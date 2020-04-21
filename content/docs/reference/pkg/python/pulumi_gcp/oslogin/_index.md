---
title: Module oslogin
title_tag: Module oslogin | Package pulumi_gcp | Python SDK
linktitle: oslogin
notitle: true
---

<div class="section" id="oslogin">
<h1>oslogin<a class="headerlink" href="#oslogin" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.oslogin"></span><dl class="class">
<dt id="pulumi_gcp.oslogin.SshPublicKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.oslogin.</code><code class="sig-name descname">SshPublicKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expiration_time_usec=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH public key information associated with a Google account.</p>
<p>To get more information about SSHPublicKey, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/oslogin/rest">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/oslogin">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiration_time_usec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An expiration time in microseconds since epoch.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Public key text in SSH format, defined by RFC4253 section 6.6.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user email.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.oslogin.SshPublicKey.expiration_time_usec">
<code class="sig-name descname">expiration_time_usec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.expiration_time_usec" title="Permalink to this definition">¶</a></dt>
<dd><p>An expiration time in microseconds since epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.oslogin.SshPublicKey.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SHA-256 fingerprint of the SSH public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.oslogin.SshPublicKey.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Public key text in SSH format, defined by RFC4253 section 6.6.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.oslogin.SshPublicKey.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user email.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.oslogin.SshPublicKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expiration_time_usec=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshPublicKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiration_time_usec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An expiration time in microseconds since epoch.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SHA-256 fingerprint of the SSH public key.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Public key text in SSH format, defined by RFC4253 section 6.6.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user email.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.oslogin.SshPublicKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.oslogin.SshPublicKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.oslogin.SshPublicKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
