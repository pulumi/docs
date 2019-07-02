---
---

<div class="section" id="module-pulumi_digitalocean">
<span id="pulumi-digitalocean"></span><h1>Pulumi DigitalOcean<a class="headerlink" href="#module-pulumi_digitalocean" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_digitalocean.Cdn">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Cdn</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_id=None</em>, <em>custom_domain=None</em>, <em>origin=None</em>, <em>ttl=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Cdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean CDN Endpoint resource for use with Spaces.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>custom_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name (FQDN) of the custom subdomain used with the CDN Endpoint.</li>
<li><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name, (FQDN) for a Space.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live for the CDN Endpoint, in seconds. Default is 3600 seconds.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Cdn.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Cdn.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the CDN Endpoint was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Cdn.custom_domain">
<code class="descname">custom_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Cdn.custom_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name (FQDN) of the custom subdomain used with the CDN Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Cdn.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Cdn.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name (FQDN) from which the CDN-backed content is served.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Cdn.origin">
<code class="descname">origin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Cdn.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name, (FQDN) for a Space.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Cdn.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Cdn.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live for the CDN Endpoint, in seconds. Default is 3600 seconds.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">certificate_id</span></code>- (Optional) The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided.</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Cdn.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Cdn.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Cdn.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Cdn.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_chain=None</em>, <em>domains=None</em>, <em>leaf_certificate=None</em>, <em>name=None</em>, <em>private_key=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Certificate resource that allows you to manage
certificates for configuring TLS termination in Load Balancers.
Certificates created with this resource can be referenced in your
Load Balancer configuration via their ID. The certificate can either
be a custom one provided by you or automatically generated one with
Let’s Encrypt.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full PEM-formatted trust chain
between the certificate authority’s certificate and your domain’s TLS
certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
<li><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of fully qualified domain names (FQDNs) for
which the certificate will be issued. The domains must be managed using
DigitalOcean’s DNS. Only valid when type is <code class="docutils literal notranslate"><span class="pre">lets_encrypt</span></code>.</li>
<li><strong>leaf_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of a PEM-formatted public
TLS certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the certificate for identification.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of a PEM-formatted private-key
corresponding to the SSL certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of certificate to provision. Can be either
<code class="docutils literal notranslate"><span class="pre">custom</span></code> or <code class="docutils literal notranslate"><span class="pre">lets_encrypt</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The full PEM-formatted trust chain
between the certificate authority’s certificate and your domain’s TLS
certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.domains">
<code class="descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>List of fully qualified domain names (FQDNs) for
which the certificate will be issued. The domains must be managed using
DigitalOcean’s DNS. Only valid when type is <code class="docutils literal notranslate"><span class="pre">lets_encrypt</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.leaf_certificate">
<code class="descname">leaf_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.leaf_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of a PEM-formatted public
TLS certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the certificate for identification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.not_after">
<code class="descname">not_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.not_after" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date of the certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of a PEM-formatted private-key
corresponding to the SSL certificate. Only valid when type is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.sha1_fingerprint">
<code class="descname">sha1_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.sha1_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SHA-1 fingerprint of the certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Certificate.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Certificate.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of certificate to provision. Can be either
<code class="docutils literal notranslate"><span class="pre">custom</span></code> or <code class="docutils literal notranslate"><span class="pre">lets_encrypt</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DatabaseCluster">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">DatabaseCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>engine=None</em>, <em>maintenance_windows=None</em>, <em>name=None</em>, <em>node_count=None</em>, <em>region=None</em>, <em>size=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean database cluster resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database engine used by the cluster (ex. <code class="docutils literal notranslate"><span class="pre">pg</span></code> for PostreSQL).</li>
<li><strong>maintenance_windows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines when the automatic maintenance should be performed for the database cluster.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database cluster.</li>
<li><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes that will be included in the cluster.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DigitalOcean region where the cluster will reside.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database droplet size associated with the cluster (ex. <code class="docutils literal notranslate"><span class="pre">db-s-1vcpu-1gb</span></code>).</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Engine version used by the cluster (ex. <code class="docutils literal notranslate"><span class="pre">11</span></code> for PostgreSQL 11).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.database" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster’s default database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.engine">
<code class="descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Database engine used by the cluster (ex. <code class="docutils literal notranslate"><span class="pre">pg</span></code> for PostreSQL).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Database cluster’s hostname.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.maintenance_windows">
<code class="descname">maintenance_windows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.maintenance_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines when the automatic maintenance should be performed for the database cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.node_count">
<code class="descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of nodes that will be included in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the cluster’s default user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Network port that the database cluster is listening on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>DigitalOcean region where the cluster will reside.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Database droplet size associated with the cluster (ex. <code class="docutils literal notranslate"><span class="pre">db-s-1vcpu-1gb</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.uri">
<code class="descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URI for connecting to the database cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.user" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for the cluster’s default user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DatabaseCluster.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Engine version used by the cluster (ex. <code class="docutils literal notranslate"><span class="pre">11</span></code> for PostgreSQL 11).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.DatabaseCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DatabaseCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DatabaseCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DnsRecord">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">DnsRecord</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>flags=None</em>, <em>name=None</em>, <em>port=None</em>, <em>priority=None</em>, <em>tag=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value=None</em>, <em>weight=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DnsRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean DNS record resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add the record to.</li>
<li><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The flags of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">CAA</span></code>. Must be between 0 and 255.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.  Must be between 1 and 65535.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">MX</span></code> or <code class="docutils literal notranslate"><span class="pre">SRV</span></code>. Must be between 0 and 65535.</li>
<li><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">CAA</span></code>. Must be one of <code class="docutils literal notranslate"><span class="pre">issue</span></code>, <code class="docutils literal notranslate"><span class="pre">wildissue</span></code>, or <code class="docutils literal notranslate"><span class="pre">iodef</span></code>.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live for the record, in seconds. Must be at least 0.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of record. Must be one of <code class="docutils literal notranslate"><span class="pre">A</span></code>, <code class="docutils literal notranslate"><span class="pre">AAAA</span></code>, <code class="docutils literal notranslate"><span class="pre">CAA</span></code>, <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>, <code class="docutils literal notranslate"><span class="pre">MX</span></code>, <code class="docutils literal notranslate"><span class="pre">NS</span></code>, <code class="docutils literal notranslate"><span class="pre">TXT</span></code>, or <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the record.</li>
<li><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The weight of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.  Must be between 0 and 65535.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to add the record to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.flags">
<code class="descname">flags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.flags" title="Permalink to this definition">¶</a></dt>
<dd><p>The flags of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">CAA</span></code>. Must be between 0 and 255.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.  Must be between 1 and 65535.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">MX</span></code> or <code class="docutils literal notranslate"><span class="pre">SRV</span></code>. Must be between 0 and 65535.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.tag">
<code class="descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">CAA</span></code>. Must be one of <code class="docutils literal notranslate"><span class="pre">issue</span></code>, <code class="docutils literal notranslate"><span class="pre">wildissue</span></code>, or <code class="docutils literal notranslate"><span class="pre">iodef</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live for the record, in seconds. Must be at least 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of record. Must be one of <code class="docutils literal notranslate"><span class="pre">A</span></code>, <code class="docutils literal notranslate"><span class="pre">AAAA</span></code>, <code class="docutils literal notranslate"><span class="pre">CAA</span></code>, <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>, <code class="docutils literal notranslate"><span class="pre">MX</span></code>, <code class="docutils literal notranslate"><span class="pre">NS</span></code>, <code class="docutils literal notranslate"><span class="pre">TXT</span></code>, or <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DnsRecord.weight">
<code class="descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The weight of the record. Only valid when type is <code class="docutils literal notranslate"><span class="pre">SRV</span></code>.  Must be between 0 and 65535.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.DnsRecord.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DnsRecord.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DnsRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Domain">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Domain</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip_address=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean domain resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the domain. If specified, this IP
is used to created an initial A record for the domain.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Domain.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Domain.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the domain. If specified, this IP
is used to created an initial A record for the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Domain.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Domain.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Domain.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name of the domain</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Domain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Domain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Droplet">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Droplet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backups=None</em>, <em>image=None</em>, <em>ipv6=None</em>, <em>monitoring=None</em>, <em>name=None</em>, <em>private_networking=None</em>, <em>region=None</em>, <em>resize_disk=None</em>, <em>size=None</em>, <em>ssh_keys=None</em>, <em>tags=None</em>, <em>user_data=None</em>, <em>volume_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Droplet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
<a class="reference external" href="https://www.terraform.io/docs/provisioners/index.html">provisioning</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling if backups are made. Defaults to
false.</li>
<li><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Droplet image ID or slug.</li>
<li><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling if IPv6 is enabled. Defaults to false.</li>
<li><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether monitoring agent is installed.
Defaults to false.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Droplet name.</li>
<li><strong>private_networking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling if private networks are
enabled. Defaults to false.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region to start in.</li>
<li><strong>resize_disk</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether to increase the disk
size when resizing a Droplet. It defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. When set to <code class="docutils literal notranslate"><span class="pre">false</span></code>,
only the Droplet’s RAM and CPU will be resized. <strong>Increasing a Droplet’s disk
size is a permanent change</strong>. Increasing only RAM and CPU is reversible.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique slug that indentifies the type of Droplet. You can find a list of available slugs on <a class="reference external" href="https://developers.digitalocean.com/documentation/v2/#list-all-sizes">DigitalOcean API documentation</a>.</li>
<li><strong>ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SSH IDs or fingerprints to enable in
the format <code class="docutils literal notranslate"><span class="pre">[12345,</span> <span class="pre">123456]</span></code>. To retrieve this info, use a tool such
as <code class="docutils literal notranslate"><span class="pre">curl</span></code> with the <a class="reference external" href="https://developers.digitalocean.com/documentation/v2/#ssh-keys">DigitalOcean API</a>,
to retrieve them.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the tags to be applied to this Droplet.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the Droplet.</li>
<li><strong>volume_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the IDs of each <a class="reference external" href="https://www.terraform.io/docs/providers/do/r/volume.html">block storage volume</a> to be attached to the Droplet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.backups">
<code class="descname">backups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling if backups are made. Defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.disk">
<code class="descname">disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the instance’s disk in GB</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.image">
<code class="descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplet image ID or slug.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.ipv4_address">
<code class="descname">ipv4_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.ipv4_address_private">
<code class="descname">ipv4_address_private</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.ipv4_address_private" title="Permalink to this definition">¶</a></dt>
<dd><p>The private networking IPv4 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.ipv6">
<code class="descname">ipv6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling if IPv6 is enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.ipv6_address">
<code class="descname">ipv6_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.ipv6_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.locked">
<code class="descname">locked</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Droplet locked</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether monitoring agent is installed.
Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplet name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.price_hourly">
<code class="descname">price_hourly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.price_hourly" title="Permalink to this definition">¶</a></dt>
<dd><p>Droplet hourly price</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.price_monthly">
<code class="descname">price_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.price_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Droplet monthly price</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.private_networking">
<code class="descname">private_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.private_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling if private networks are
enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region to start in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.resize_disk">
<code class="descname">resize_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.resize_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether to increase the disk
size when resizing a Droplet. It defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. When set to <code class="docutils literal notranslate"><span class="pre">false</span></code>,
only the Droplet’s RAM and CPU will be resized. <strong>Increasing a Droplet’s disk
size is a permanent change</strong>. Increasing only RAM and CPU is reversible.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique slug that indentifies the type of Droplet. You can find a list of available slugs on <a class="reference external" href="https://developers.digitalocean.com/documentation/v2/#list-all-sizes">DigitalOcean API documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.ssh_keys">
<code class="descname">ssh_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SSH IDs or fingerprints to enable in
the format <code class="docutils literal notranslate"><span class="pre">[12345,</span> <span class="pre">123456]</span></code>. To retrieve this info, use a tool such
as <code class="docutils literal notranslate"><span class="pre">curl</span></code> with the <a class="reference external" href="https://developers.digitalocean.com/documentation/v2/#ssh-keys">DigitalOcean API</a>,
to retrieve them.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Droplet</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the tags to be applied to this Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name of the Droplet</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">name</span></code>- The name of the Droplet</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A string of the desired User Data for the Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.vcpus">
<code class="descname">vcpus</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.vcpus" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of the instance’s virtual CPUs</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Droplet.volume_ids">
<code class="descname">volume_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Droplet.volume_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the IDs of each <a class="reference external" href="https://www.terraform.io/docs/providers/do/r/volume.html">block storage volume</a> to be attached to the Droplet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Droplet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Droplet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Droplet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Droplet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DropletSnapshot">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">DropletSnapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>droplet_id=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which can be used to create a snapshot from an existing DigitalOcean Droplet.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>droplet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Droplet from which the snapshot will be taken.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the Droplet snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the Droplet snapshot was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.droplet_id">
<code class="descname">droplet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.droplet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Droplet from which the snapshot will be taken.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.min_disk_size">
<code class="descname">min_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.min_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size in gigabytes required for a Droplet to be created based on this snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the Droplet snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.regions">
<code class="descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DigitalOcean region “slugs” indicating where the droplet snapshot is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.DropletSnapshot.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The billable size of the Droplet snapshot in gigabytes.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.DropletSnapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.DropletSnapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.DropletSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Firewall">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Firewall</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>droplet_ids=None</em>, <em>inbound_rules=None</em>, <em>name=None</em>, <em>outbound_rules=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>droplet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of the IDs of the Droplets assigned
to the Firewall.</li>
<li><strong>inbound_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The inbound access rule block for the Firewall.
The <code class="docutils literal notranslate"><span class="pre">inbound_rule</span></code> block is documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall name</li>
<li><strong>outbound_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The outbound access rule block for the Firewall.
The <code class="docutils literal notranslate"><span class="pre">outbound_rule</span></code> block is documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The names of the Tags assigned to the Firewall.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>A time value given in ISO8601 combined date and time format
that represents when the Firewall was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.droplet_ids">
<code class="descname">droplet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.droplet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of the IDs of the Droplets assigned
to the Firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.inbound_rules">
<code class="descname">inbound_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.inbound_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The inbound access rule block for the Firewall.
The <code class="docutils literal notranslate"><span class="pre">inbound_rule</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Firewall name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.outbound_rules">
<code class="descname">outbound_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.outbound_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The outbound access rule block for the Firewall.
The <code class="docutils literal notranslate"><span class="pre">outbound_rule</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.pending_changes">
<code class="descname">pending_changes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.pending_changes" title="Permalink to this definition">¶</a></dt>
<dd><p>An list of object containing the fields, “droplet_id”,
“removing”, and “status”.  It is provided to detail exactly which Droplets
are having their security policies updated.  When empty, all changes
have been successfully applied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.status" title="Permalink to this definition">¶</a></dt>
<dd><p>A status string indicating the current state of the Firewall.
This can be “waiting”, “succeeded”, or “failed”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Firewall.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Firewall.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the Tags assigned to the Firewall.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Firewall.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Firewall.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.FloatingIp">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">FloatingIp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>droplet_id=None</em>, <em>ip_address=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Floating IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets.</p>
<blockquote>
<div><strong>NOTE:</strong> Floating IPs can be assigned to a Droplet either directly on the <code class="docutils literal notranslate"><span class="pre">digitalocean_floating_ip</span></code> resource by setting a <code class="docutils literal notranslate"><span class="pre">droplet_id</span></code> or using the <code class="docutils literal notranslate"><span class="pre">digitalocean_floating_ip_assignment</span></code> resource, but the two cannot be used together.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>droplet_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of Droplet that the Floating IP will be assigned to.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Address of the resource</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region that the Floating IP is reserved to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIp.droplet_id">
<code class="descname">droplet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.droplet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of Droplet that the Floating IP will be assigned to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIp.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP Address of the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIp.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region that the Floating IP is reserved to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIp.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name of the floating ip</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.FloatingIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.FloatingIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.FloatingIpAssignment">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">FloatingIpAssignment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>droplet_id=None</em>, <em>ip_address=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIpAssignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for assigning an existing DigitalOcean Floating IP to a Droplet. This
makes it easy to provision floating IP addresses that are not tied to the lifecycle of your
Droplet.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>droplet_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of Droplet that the Floating IP will be assigned to.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Floating IP to assign to the Droplet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIpAssignment.droplet_id">
<code class="descname">droplet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIpAssignment.droplet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of Droplet that the Floating IP will be assigned to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.FloatingIpAssignment.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.FloatingIpAssignment.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Floating IP to assign to the Droplet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.FloatingIpAssignment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIpAssignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.FloatingIpAssignment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.FloatingIpAssignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.GetCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetCertificateResult</code><span class="sig-paren">(</span><em>domains=None</em>, <em>name=None</em>, <em>not_after=None</em>, <em>sha1_fingerprint=None</em>, <em>state=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetCertificateResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetDomainResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetDomainResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>ttl=None</em>, <em>urn=None</em>, <em>zone_file=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomain.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetDomainResult.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDomainResult.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name of the domain</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">zone_file</span></code>: The zone file of the domain.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDomainResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDomainResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetDropletResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetDropletResult</code><span class="sig-paren">(</span><em>backups=None</em>, <em>disk=None</em>, <em>image=None</em>, <em>ipv4_address=None</em>, <em>ipv4_address_private=None</em>, <em>ipv6=None</em>, <em>ipv6_address=None</em>, <em>ipv6_address_private=None</em>, <em>locked=None</em>, <em>memory=None</em>, <em>monitoring=None</em>, <em>name=None</em>, <em>price_hourly=None</em>, <em>price_monthly=None</em>, <em>private_networking=None</em>, <em>region=None</em>, <em>size=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>urn=None</em>, <em>vcpus=None</em>, <em>volume_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDroplet.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.backups">
<code class="descname">backups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether backups are enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.disk">
<code class="descname">disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Droplets disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.image">
<code class="descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplet image ID or slug.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.ipv4_address">
<code class="descname">ipv4_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplets public IPv4 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.ipv4_address_private">
<code class="descname">ipv4_address_private</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.ipv4_address_private" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplets private IPv4 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.ipv6">
<code class="descname">ipv6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.ipv6_address">
<code class="descname">ipv6_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.ipv6_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplets public IPv6 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.ipv6_address_private">
<code class="descname">ipv6_address_private</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.ipv6_address_private" title="Permalink to this definition">¶</a></dt>
<dd><p>The Droplets private IPv6 address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.locked">
<code class="descname">locked</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the Droplet is locked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.memory">
<code class="descname">memory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.memory" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of the Droplets memory in MB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether monitoring agent is installed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.price_hourly">
<code class="descname">price_hourly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.price_hourly" title="Permalink to this definition">¶</a></dt>
<dd><p>Droplet hourly price.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.price_monthly">
<code class="descname">price_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.price_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Droplet monthly price.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.private_networking">
<code class="descname">private_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.private_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether private networks are enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the Droplet is running in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique slug that indentifies the type of Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the tags associated to the Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name of the Droplet</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.vcpus">
<code class="descname">vcpus</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.vcpus" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of the Droplets virtual CPUs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.volume_ids">
<code class="descname">volume_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.volume_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the IDs of each volumes attached to the Droplet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetDropletSnapshotResult</code><span class="sig-paren">(</span><em>created_at=None</em>, <em>droplet_id=None</em>, <em>min_disk_size=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>name_regex=None</em>, <em>region=None</em>, <em>regions=None</em>, <em>size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDropletSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the Droplet snapshot was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.droplet_id">
<code class="descname">droplet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.droplet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Droplet from which the Droplet snapshot originated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.min_disk_size">
<code class="descname">min_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.min_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size in gigabytes required for a Droplet to be created based on this Droplet snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.regions">
<code class="descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DigitalOcean region “slugs” indicating where the Droplet snapshot is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The billable size of the Droplet snapshot in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetDropletSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetDropletSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetFloatingIpResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetFloatingIpResult</code><span class="sig-paren">(</span><em>droplet_id=None</em>, <em>ip_address=None</em>, <em>region=None</em>, <em>urn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFloatingIp.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetFloatingIpResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetFloatingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetImageResult</code><span class="sig-paren">(</span><em>distribution=None</em>, <em>image=None</em>, <em>min_disk_size=None</em>, <em>name=None</em>, <em>private=None</em>, <em>regions=None</em>, <em>slug=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetImageResult.distribution">
<code class="descname">distribution</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetImageResult.distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the distribution of the OS of the image.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">min_disk_size</span></code>: The minimum ‘disk’ required for the image.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetImageResult.image">
<code class="descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetImageResult.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetImageResult.private">
<code class="descname">private</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetImageResult.private" title="Permalink to this definition">¶</a></dt>
<dd><p>Is image a public image or not. Public images represent
Linux distributions or One-Click Applications, while non-public images represent
snapshots and backups and are only available within your account.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">regions</span></code>: The regions that the image is available in.</li>
<li><code class="docutils literal notranslate"><span class="pre">type</span></code>: Type of the image.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em>cluster_subnet=None</em>, <em>created_at=None</em>, <em>endpoint=None</em>, <em>ipv4_address=None</em>, <em>kube_configs=None</em>, <em>name=None</em>, <em>node_pools=None</em>, <em>region=None</em>, <em>service_subnet=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>updated_at=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesCluster.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.cluster_subnet">
<code class="descname">cluster_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.cluster_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of IP addresses in the overlay network of the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the Kubernetes cluster was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.ipv4_address">
<code class="descname">ipv4_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IPv4 address of the Kubernetes master node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.node_pools">
<code class="descname">node_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.node_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of node pools associated with the cluster. Each node pool exports the following attributes:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">id</span></code> -  The unique ID that can be used to identify and reference the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - The name of the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">size</span></code> - The slug identifier for the type of Droplet used as workers in the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">node_count</span></code> - The number of Droplet instances in the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">tags</span></code> - A list of tag names applied to the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">nodes</span></code> - A list of nodes in the pool. Each node exports the following attributes:</li>
<li><code class="docutils literal notranslate"><span class="pre">id</span></code> -  A unique ID that can be used to identify and reference the node.</li>
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - The auto-generated name for the node.</li>
<li><code class="docutils literal notranslate"><span class="pre">status</span></code> -  A string indicating the current status of the individual node.</li>
<li><code class="docutils literal notranslate"><span class="pre">created_at</span></code> - The date and time when the node was created.</li>
<li><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> - The date and time when the node was last updated.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug identifier for the region where the Kubernetes cluster is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.service_subnet">
<code class="descname">service_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.service_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of assignable IP addresses for services running in the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>A string indicating the current status of the cluster. Potential values include running, provisioning, and errored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag names to be applied to the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the Kubernetes cluster was last updated.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">kube_config.0</span></code> - A representation of the Kubernetes cluster’s kubeconfig with the following attributes:</li>
<li><code class="docutils literal notranslate"><span class="pre">raw_config</span></code> - The full contents of the Kubernetes cluster’s kubeconfig file.</li>
<li><code class="docutils literal notranslate"><span class="pre">host</span></code> - The URL of the API server on the Kubernetes master node.</li>
<li><code class="docutils literal notranslate"><span class="pre">client_key</span></code> - The base64 encoded private key used by clients to access the cluster.</li>
<li><code class="docutils literal notranslate"><span class="pre">client_certificate</span></code> - The base64 encoded public certificate used by clients to access the cluster.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_ca_certificate</span></code> - The base64 encoded public certificate for the cluster’s certificate authority.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug identifier for the version of Kubernetes used for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetKubernetesClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetKubernetesClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetLoadBalancerResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em>algorithm=None</em>, <em>droplet_ids=None</em>, <em>droplet_tag=None</em>, <em>enable_proxy_protocol=None</em>, <em>forwarding_rules=None</em>, <em>healthcheck=None</em>, <em>ip=None</em>, <em>name=None</em>, <em>redirect_http_to_https=None</em>, <em>region=None</em>, <em>status=None</em>, <em>sticky_sessions=None</em>, <em>urn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetLoadBalancerResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetLoadBalancerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetRecordResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetRecordResult</code><span class="sig-paren">(</span><em>data=None</em>, <em>domain=None</em>, <em>flags=None</em>, <em>name=None</em>, <em>port=None</em>, <em>priority=None</em>, <em>tag=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>weight=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetRecordResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRecord.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetRecordResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetRecordResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetSshKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetSshKeyResult</code><span class="sig-paren">(</span><em>fingerprint=None</em>, <em>name=None</em>, <em>public_key=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetSshKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetSshKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetTagResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetTagResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetTagResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTag.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetTagResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetTagResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetVolumeResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetVolumeResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>droplet_ids=None</em>, <em>filesystem_label=None</em>, <em>filesystem_type=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>urn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Text describing a block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.droplet_ids">
<code class="descname">droplet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.droplet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of associated Droplet ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.filesystem_label">
<code class="descname">filesystem_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.filesystem_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Filesystem label currently in-use on the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.filesystem_type">
<code class="descname">filesystem_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.filesystem_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Filesystem type currently in-use on the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the block storage volume in GiB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">GetVolumeSnapshotResult</code><span class="sig-paren">(</span><em>created_at=None</em>, <em>min_disk_size=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>name_regex=None</em>, <em>region=None</em>, <em>regions=None</em>, <em>size=None</em>, <em>volume_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolumeSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the volume snapshot was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.min_disk_size">
<code class="descname">min_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.min_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size in gigabytes required for a volume to be created based on this volume snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.regions">
<code class="descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DigitalOcean region “slugs” indicating where the volume snapshot is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The billable size of the volume snapshot in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the volume from which the volume snapshot originated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.GetVolumeSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.GetVolumeSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_digitalocean.KubernetesCluster">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">KubernetesCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>node_pool=None</em>, <em>region=None</em>, <em>tags=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>NOTE:</strong> DigitalOcean Kubernetes is currently in <a class="reference external" href="https://www.digitalocean.com/docs/platform/product-lifecycle/">Limited Availability</a>. In order to access its API, you must first enable Kubernetes on your account by opting-in via the <a class="reference external" href="https://cloud.digitalocean.com/kubernetes/clusters">cloud control panel</a>. While the Kubernetes Cluster functionality is currently in limited availability the structure of this resource may change over time. Please share any feedback you may have by <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-digitalocean/issues">opening an issue on GitHub</a>.</div></blockquote>
<p>Provides a DigitalOcean Kubernetes cluster resource. This can be used to create, delete, and modify clusters. For more information see the <a class="reference external" href="https://www.digitalocean.com/docs/kubernetes/">official documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the Kubernetes cluster.</li>
<li><strong>node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block representing the cluster’s default node pool. Additional node pools may be added to the cluster using the <code class="docutils literal notranslate"><span class="pre">digitalocean_kubernetes_node_pool</span></code> resource. The following arguments may be specified:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The slug identifier for the region where the Kubernetes cluster will be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag names to be applied to the Kubernetes cluster.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The slug identifier for the version of Kubernetes used for the cluster.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.cluster_subnet">
<code class="descname">cluster_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.cluster_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of IP addresses in the overlay network of the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the Kubernetes cluster was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.ipv4_address">
<code class="descname">ipv4_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IPv4 address of the Kubernetes master node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.node_pool">
<code class="descname">node_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.node_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>A block representing the cluster’s default node pool. Additional node pools may be added to the cluster using the <code class="docutils literal notranslate"><span class="pre">digitalocean_kubernetes_node_pool</span></code> resource. The following arguments may be specified:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) A name for the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">size</span></code> - (Required) The slug identifier for the type of Droplet to be used as workers in the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">node_count</span></code> - (Required) The number of Droplet instances in the node pool.</li>
<li><code class="docutils literal notranslate"><span class="pre">tags</span></code> - (Optional) A list of tag names to be applied to the Kubernetes cluster.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug identifier for the region where the Kubernetes cluster will be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.service_subnet">
<code class="descname">service_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.service_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of assignable IP addresses for services running in the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>A string indicating the current status of the cluster. Potential values include running, provisioning, and errored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag names to be applied to the Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the Kubernetes cluster was last updated.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">kube_config.0</span></code> - A representation of the Kubernetes cluster’s kubeconfig with the following attributes:</li>
<li><code class="docutils literal notranslate"><span class="pre">raw_config</span></code> - The full contents of the Kubernetes cluster’s kubeconfig file.</li>
<li><code class="docutils literal notranslate"><span class="pre">host</span></code> - The URL of the API server on the Kubernetes master node.</li>
<li><code class="docutils literal notranslate"><span class="pre">client_key</span></code> - The base64 encoded private key used by clients to access the cluster.</li>
<li><code class="docutils literal notranslate"><span class="pre">client_certificate</span></code> - The base64 encoded public certificate used by clients to access the cluster.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_ca_certificate</span></code> - The base64 encoded public certificate for the cluster’s certificate authority.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesCluster.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug identifier for the version of Kubernetes used for the cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.KubernetesCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.KubernetesCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.KubernetesNodePool">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">KubernetesNodePool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_id=None</em>, <em>name=None</em>, <em>node_count=None</em>, <em>size=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>NOTE:</strong> DigitalOcean Kubernetes is currently in <a class="reference external" href="https://www.digitalocean.com/docs/platform/product-lifecycle/">Limited Availability</a>. In order to access its API, you must first enable Kubernetes on your account by opting-in via the <a class="reference external" href="https://cloud.digitalocean.com/kubernetes/clusters">cloud control panel</a>. While the Kubernetes Cluster functionality is currently in limited availability the structure of this resource may change over time. Please share any feedback you may have by <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-digitalocean/issues">opening an issue on GitHub</a>.</div></blockquote>
<p>Provides a DigitalOcean Kubernetes node pool resource. While the default node pool must be defined in the <code class="docutils literal notranslate"><span class="pre">digitalocean_kubernetes_cluster</span></code> resource, this resource can be used to add additional ones to a cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Kubernetes cluster to which the node pool is associated.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the node pool.</li>
<li><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Droplet instances in the node pool.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The slug identifier for the type of Droplet to be used as workers in the node pool.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag names to be applied to the Kubernetes cluster.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.cluster_id">
<code class="descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Kubernetes cluster to which the node pool is associated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the node pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.node_count">
<code class="descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Droplet instances in the node pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.nodes">
<code class="descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of nodes in the pool. Each node exports the following attributes:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">id</span></code> -  A unique ID that can be used to identify and reference the node.</li>
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - The auto-generated name for the node.</li>
<li><code class="docutils literal notranslate"><span class="pre">status</span></code> -  A string indicating the current status of the individual node.</li>
<li><code class="docutils literal notranslate"><span class="pre">created_at</span></code> - The date and time when the node was created.</li>
<li><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> - The date and time when the node was last updated.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug identifier for the type of Droplet to be used as workers in the node pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.KubernetesNodePool.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag names to be applied to the Kubernetes cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.KubernetesNodePool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.KubernetesNodePool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.KubernetesNodePool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.LoadBalancer">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">LoadBalancer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>algorithm=None</em>, <em>droplet_ids=None</em>, <em>droplet_tag=None</em>, <em>enable_proxy_protocol=None</em>, <em>forwarding_rules=None</em>, <em>healthcheck=None</em>, <em>name=None</em>, <em>redirect_http_to_https=None</em>, <em>region=None</em>, <em>sticky_sessions=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancing algorithm used to determine
which backend Droplet will be selected by a client. It must be either <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>
or <code class="docutils literal notranslate"><span class="pre">least_connections</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>.</li>
<li><strong>droplet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the IDs of each droplet to be attached to the Load Balancer.</li>
<li><strong>droplet_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Droplet tag corresponding to Droplets to be assigned to the Load Balancer.</li>
<li><strong>enable_proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value indicating whether PROXY
Protocol should be used to pass information from connecting client requests to
the backend service. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>forwarding_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">forwarding_rule</span></code> to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">forwarding_rule</span></code> block is documented below.</li>
<li><strong>healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> block to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> block is documented below. Only 1 healthcheck is allowed.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer name</li>
<li><strong>redirect_http_to_https</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value indicating whether
HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.
Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region to start in</li>
<li><strong>sticky_sessions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sticky_sessions</span></code> block to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">sticky_sessions</span></code> block is documented below. Only 1 sticky_sessions block is allowed.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.algorithm">
<code class="descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancing algorithm used to determine
which backend Droplet will be selected by a client. It must be either <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>
or <code class="docutils literal notranslate"><span class="pre">least_connections</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.droplet_ids">
<code class="descname">droplet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.droplet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the IDs of each droplet to be attached to the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.droplet_tag">
<code class="descname">droplet_tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.droplet_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Droplet tag corresponding to Droplets to be assigned to the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.enable_proxy_protocol">
<code class="descname">enable_proxy_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.enable_proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value indicating whether PROXY
Protocol should be used to pass information from connecting client requests to
the backend service. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.forwarding_rules">
<code class="descname">forwarding_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.forwarding_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">forwarding_rule</span></code> to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">forwarding_rule</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.healthcheck">
<code class="descname">healthcheck</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> block to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> block is documented below. Only 1 healthcheck is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancer name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.redirect_http_to_https">
<code class="descname">redirect_http_to_https</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.redirect_http_to_https" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value indicating whether
HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.
Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region to start in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.sticky_sessions">
<code class="descname">sticky_sessions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.sticky_sessions" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sticky_sessions</span></code> block to be assigned to the
Load Balancer. The <code class="docutils literal notranslate"><span class="pre">sticky_sessions</span></code> block is documented below. Only 1 sticky_sessions block is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.LoadBalancer.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name for the Load Balancer</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.LoadBalancer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.LoadBalancer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Project">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>environment=None</em>, <em>name=None</em>, <em>purpose=None</em>, <em>resources=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Project resource.</p>
<p>Projects allow you to organize your resources into groups that fit the way you work.
You can group resources (like Droplets, Spaces, Load Balancers, domains, and Floating IPs)
in ways that align with the applications you host on DigitalOcean.</p>
<p>The following resources can be associated with a project:</p>
<ul class="simple">
<li>Droplet</li>
<li>Load Balancer</li>
<li>Domain</li>
<li>Volume</li>
<li>Floating IP</li>
<li>Spaces Bucket</li>
</ul>
<p><strong>Note:</strong> A Terrafrom managed project cannot be set as a default project.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the description of the project</li>
<li><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the environment of the project’s resources. The possible values are: <code class="docutils literal notranslate"><span class="pre">Development</span></code>, <code class="docutils literal notranslate"><span class="pre">Staging</span></code>, <code class="docutils literal notranslate"><span class="pre">Production</span></code>)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Project</li>
<li><strong>purpose</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the purpose of the project, (Default: “Web Application”)</li>
<li><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a list of uniform resource names (URNs) for the resources associated with the project</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Project.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>the date and time when the project was created, (ISO8601)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>the description of the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.environment">
<code class="descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>the environment of the project’s resources. The possible values are: <code class="docutils literal notranslate"><span class="pre">Development</span></code>, <code class="docutils literal notranslate"><span class="pre">Staging</span></code>, <code class="docutils literal notranslate"><span class="pre">Production</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the id of the project owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.owner_uuid">
<code class="descname">owner_uuid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.owner_uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>the unique universal identifier of the project owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.purpose">
<code class="descname">purpose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.purpose" title="Permalink to this definition">¶</a></dt>
<dd><p>the purpose of the project, (Default: “Web Application”)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.resources">
<code class="descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>a list of uniform resource names (URNs) for the resources associated with the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Project.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Project.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>the date and time when the project was last updated, (ISO8601)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Project.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Project.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Provider">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_endpoint=None</em>, <em>spaces_access_id=None</em>, <em>spaces_secret_key=None</em>, <em>token=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the digitalocean package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="pulumi_digitalocean.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.SpacesBucket">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">SpacesBucket</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>acl=None</em>, <em>force_destroy=None</em>, <em>name=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a bucket resource for Spaces, DigitalOcean’s object storage product.</p>
<p>The <a class="reference external" href="https://developers.digitalocean.com/documentation/spaces/">Spaces API</a> was
designed to be interoperable with Amazon’s AWS S3 API. This allows users to
interact with the service while using the tools they already know. Spaces
mirrors S3’s authentication framework and requests to Spaces require a key pair
similar to Amazon’s Access ID and Secret Key.</p>
<p>The authentication requirement can be met by either setting the
<code class="docutils literal notranslate"><span class="pre">SPACES_ACCESS_KEY_ID</span></code> and <code class="docutils literal notranslate"><span class="pre">SPACES_SECRET_ACCESS_KEY</span></code> environment variables or
the provider’s <code class="docutils literal notranslate"><span class="pre">spaces_access_id</span></code> and <code class="docutils literal notranslate"><span class="pre">spaces_secret_key</span></code> arguments to the
access ID and secret you generate via the DigitalOcean control panel. For
example:</p>
<p>For more information, See <a class="reference external" href="https://www.digitalocean.com/community/tutorials/an-introduction-to-digitalocean-spaces">An Introduction to DigitalOcean Spaces</a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Canned ACL applied on bucket creation (<code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public-read</span></code>)</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Unless <code class="docutils literal notranslate"><span class="pre">true</span></code>, the bucket will only be destroyed if empty (Defalts to <code class="docutils literal notranslate"><span class="pre">false</span></code>)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the bucket resides (Defaults to <code class="docutils literal notranslate"><span class="pre">nyc3</span></code>)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.acl">
<code class="descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Canned ACL applied on bucket creation (<code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public-read</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.bucket_domain_name">
<code class="descname">bucket_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.bucket_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the bucket (e.g. bucket-name.nyc3.digitaloceanspaces.com)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Unless <code class="docutils literal notranslate"><span class="pre">true</span></code>, the bucket will only be destroyed if empty (Defalts to <code class="docutils literal notranslate"><span class="pre">false</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the bucket resides (Defaults to <code class="docutils literal notranslate"><span class="pre">nyc3</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SpacesBucket.urn">
<code class="descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The uniform resource name for the bucket</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.SpacesBucket.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.SpacesBucket.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SpacesBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.SshKey">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">SshKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>public_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean SSH key resource to allow you to manage SSH
keys for Droplet access. Keys created with this resource
can be referenced in your Droplet configuration via their ID or
fingerprint.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.SshKey.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SshKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.SshKey.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.SshKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.SshKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Tag">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Tag</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Tag resource. A Tag is a label that can be applied to a
Droplet resource in order to better organize or facilitate the lookups and
actions on it. Tags created with this resource can be referenced in your Droplet
configuration via their ID or name.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tag</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Tag.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Tag.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tag</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Tag.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Tag.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Tag.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Tag.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Volume">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">Volume</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>filesystem_type=None</em>, <em>initial_filesystem_label=None</em>, <em>initial_filesystem_type=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free-form text field up to a limit of 1024 bytes to describe a block storage volume.</li>
<li><strong>filesystem_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Filesystem type (<code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code>) for the block storage volume.</li>
<li><strong>initial_filesystem_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Initial filesystem label for the block storage volume.</li>
<li><strong>initial_filesystem_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Initial filesystem type (<code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code>) for the block storage volume.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and “-“, up to a limit of 64 characters.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region that the block storage volume will be created in.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the block storage volume in GiB. If updated, can only be expanded.</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A free-form text field up to a limit of 1024 bytes to describe a block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.droplet_ids">
<code class="descname">droplet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.droplet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of associated droplet ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.filesystem_label">
<code class="descname">filesystem_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.filesystem_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Filesystem label for the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.filesystem_type">
<code class="descname">filesystem_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.filesystem_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Filesystem type (<code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code>) for the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.initial_filesystem_label">
<code class="descname">initial_filesystem_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.initial_filesystem_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Initial filesystem label for the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.initial_filesystem_type">
<code class="descname">initial_filesystem_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.initial_filesystem_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Initial filesystem type (<code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code>) for the block storage volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and “-“, up to a limit of 64 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region that the block storage volume will be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the block storage volume in GiB. If updated, can only be expanded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.Volume.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.Volume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.Volume.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.Volume.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.VolumeAttachment">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">VolumeAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>droplet_id=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages attaching a Volume to a Droplet.</p>
<blockquote>
<div><strong>NOTE:</strong> Volumes can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">digitalocean_droplet</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">digitalocean_volume_attachment</span></code> resource - but the two cannot be used together. If both are used against the same Droplet, the volume attachments will constantly drift.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>droplet_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Droplet to attach the volume to.</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Volume to be attached to the Droplet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeAttachment.droplet_id">
<code class="descname">droplet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeAttachment.droplet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Droplet to attach the volume to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeAttachment.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Volume to be attached to the Droplet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.VolumeAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.VolumeAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.VolumeSnapshot">
<em class="property">class </em><code class="descclassname">pulumi_digitalocean.</code><code class="descname">VolumeSnapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DigitalOcean Volume Snapshot which can be used to create a snapshot from an existing volume.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the volume snapshot.</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the volume from which the volume snapshot originated.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the volume snapshot was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.min_disk_size">
<code class="descname">min_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.min_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size in gigabytes required for a volume to be created based on this volume snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the volume snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.regions">
<code class="descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DigitalOcean region “slugs” indicating where the volume snapshot is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The billable size of the volume snapshot in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_digitalocean.VolumeSnapshot.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the volume from which the volume snapshot originated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_digitalocean.VolumeSnapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.VolumeSnapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.VolumeSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_digitalocean.get_certificate">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_certificate</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a certificate. This data source provides the name, type, state,
domains, expiry date, and the sha1 fingerprint as configured on your DigitalOcean account.
This is useful if the certificate in question is not managed by Terraform or you need to utilize
any of the certificates data.</p>
<p>An error is triggered if the provided certificate name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_domain">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_domain</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a domain. This data source provides the name, TTL, and zone
file as configured on your DigitalOcean account. This is useful if the domain
name in question is not managed by Terraform or you need to utilize TTL or zone
file data.</p>
<p>An error is triggered if the provided domain name is not managed with your
DigitalOcean account.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_droplet">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_droplet</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_droplet" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a Droplet for use in other resources. This data source provides
all of the Droplet’s properties as configured on your DigitalOcean account. This
is useful if the Droplet in question is not managed by Terraform or you need to
utilize any of the Droplets data.</p>
<p>An error is triggered if the provided Droplet name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_droplet_snapshot">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_droplet_snapshot</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name=None</em>, <em>name_regex=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_droplet_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Droplet snapshots are saved instances of a Droplet. Use this data
source to retrieve the ID of a DigitalOcean Droplet snapshot for use in other
resources.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_floating_ip">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_floating_ip</code><span class="sig-paren">(</span><em>ip_address=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a floating ip. This data source provides the region and Droplet id
as configured on your DigitalOcean account. This is useful if the floating IP
in question is not managed by Terraform or you need to find the Droplet the IP is
attached to.</p>
<p>An error is triggered if the provided floating IP does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_image">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_image</code><span class="sig-paren">(</span><em>name=None</em>, <em>slug=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an images for use in other resources (e.g. creating a Droplet
based on snapshot). This data source provides all of the image properties as
configured on your DigitalOcean account. This is useful if the image in question
is not managed by Terraform or you need to utilize any of the image’s data.</p>
<p>An error is triggered if zero or more than one result is returned by the query.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_kubernetes_cluster">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em>name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_kubernetes_cluster" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>NOTE:</strong> DigitalOcean Kubernetes is currently in <a class="reference external" href="https://www.digitalocean.com/docs/platform/product-lifecycle/">Limited Availability</a>. In order to access its API, you must first enable Kubernetes on your account by opting-in via the <a class="reference external" href="https://cloud.digitalocean.com/kubernetes/clusters">cloud control panel</a>. While the Kubernetes Cluster functionality is currently in limited availability the structure of this resource may change over time. Please share any feedback you may have by <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-digitalocean/issues">opening an issue on GitHub</a>.</div></blockquote>
<p>Retrieves information about a DigitalOcean Kubernetes cluster for use in other resources. This data source provides all of the cluster’s properties as configured on your DigitalOcean account. This is useful if the cluster in question is not managed by Terraform.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_load_balancer">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_load_balancer</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a load balancer for use in other resources. This data source
provides all of the load balancers properties as configured on your DigitalOcean
account. This is useful if the load balancer in question is not managed by
Terraform or you need to utilize any of the load balancers data.</p>
<p>An error is triggered if the provided load balancer name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_record">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_record</code><span class="sig-paren">(</span><em>domain=None</em>, <em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_record" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a DNS record. This data source provides the name, TTL, and zone
file as configured on your DigitalOcean account. This is useful if the record
in question is not managed by Terraform.</p>
<p>An error is triggered if the provided domain name or record are not managed with
your DigitalOcean account.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_ssh_key">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_ssh_key</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a ssh key. This data source provides the name, public key,
and fingerprint as configured on your DigitalOcean account. This is useful if
the ssh key in question is not managed by Terraform or you need to utilize any
of the keys data.</p>
<p>An error is triggered if the provided ssh key name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_tag">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_tag</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a tag. This data source provides the name as configured on
your DigitalOcean account. This is useful if the tag name in question is not
managed by Terraform or you need validate if the tag exists in the account.</p>
<p>An error is triggered if the provided tag name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_volume">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_volume</code><span class="sig-paren">(</span><em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a volume for use in other resources. This data source provides
all of the volumes properties as configured on your DigitalOcean account. This is
useful if the volume in question is not managed by Terraform or you need to utilize
any of the volumes data.</p>
<p>An error is triggered if the provided volume name does not exist.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_digitalocean.get_volume_snapshot">
<code class="descclassname">pulumi_digitalocean.</code><code class="descname">get_volume_snapshot</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name=None</em>, <em>name_regex=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_digitalocean.get_volume_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume snapshots are saved instances of a block storage volume. Use this data
source to retrieve the ID of a DigitalOcean volume snapshot for use in other
resources.</p>
</dd></dl>

</div>
