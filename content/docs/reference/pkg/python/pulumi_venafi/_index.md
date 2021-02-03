---
title: Package pulumi_venafi
title_tag: Package pulumi_venafi | Python SDK
linktitle: pulumi_venafi
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "venafi" >}}

<div class="section" id="pulumi-venafi">
<h1>Pulumi Venafi<a class="headerlink" href="#pulumi-venafi" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-venafi">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-venafi/issues">pulumi/pulumi-venafi repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-venafi/issues">terraform-providers/terraform-provider-venafi repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_venafi"></span><dl class="py class">
<dt id="pulumi_venafi.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_venafi.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_dn</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr_pem</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecdsa_curve</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_hint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pkcs12</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_pem</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_bits</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_dns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_emails</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_ips</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_days</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Certificate" title="Permalink to this definition"></a></dt>
<dd><p>Provides access to TLS key and certificate data enrolled using Venafi. This can be used to define a
certificate.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">Certificate</span></code> resource handles certificate renewals as long as a
<code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code> is run within the <code class="docutils literal notranslate"><span class="pre">expiration_window</span></code> period. Keep in mind that the
<code class="docutils literal notranslate"><span class="pre">expiration_window</span></code> in the provider configuration needs to align with the renewal
window of the issuing CA to achieve the desired result.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_venafi</span> <span class="k">as</span> <span class="nn">venafi</span>

<span class="n">webserver</span> <span class="o">=</span> <span class="n">venafi</span><span class="o">.</span><span class="n">Certificate</span><span class="p">(</span><span class="s2">&quot;webserver&quot;</span><span class="p">,</span>
    <span class="n">algorithm</span><span class="o">=</span><span class="s2">&quot;RSA&quot;</span><span class="p">,</span>
    <span class="n">common_name</span><span class="o">=</span><span class="s2">&quot;web.venafi.example&quot;</span><span class="p">,</span>
    <span class="n">custom_fields</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Cost Center&quot;</span><span class="p">:</span> <span class="s2">&quot;AB1234&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Environment&quot;</span><span class="p">:</span> <span class="s2">&quot;UAT|Staging&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">key_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;pk_pass&quot;</span><span class="p">],</span>
    <span class="n">rsa_bits</span><span class="o">=</span><span class="mi">2048</span><span class="p">,</span>
    <span class="n">san_dns</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;web01.venafi.example&quot;</span><span class="p">,</span>
        <span class="s2">&quot;web02.venafi.example&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key encryption algorithm, either <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">ECDSA</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">RSA</span></code>.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common name of the certificate.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>custom_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Collection of Custom Field name-value pairs to
assign to the certificate.</p></li>
<li><p><strong>ecdsa_curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ECDSA curve to use when generating a key</p></li>
<li><p><strong>expiration_window</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of hours before certificate expiry
to request a new certificate.</p></li>
<li><p><strong>issuer_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used with valid_days to indicate the target
issuer when using Trust Protection Platform.  Relevant values are: “DigiCert”,
“Entrust”, and “Microsoft”.</p></li>
<li><p><strong>key_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to encrypt the private key.</p></li>
<li><p><strong>pkcs12</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A base64-encoded PKCS#12 keystore secured by the <code class="docutils literal notranslate"><span class="pre">key_password</span></code>.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key in PEM format.</p></li>
<li><p><strong>rsa_bits</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of bits to use when generating an RSA key.
Applies when <code class="docutils literal notranslate"><span class="pre">algorithm=RSA</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p></li>
<li><p><strong>san_dns</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of DNS names to use as alternative
subjects of the certificate.</p></li>
<li><p><strong>san_emails</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of email addresses to use as
alternative subjects of the certificate.</p></li>
<li><p><strong>san_ips</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of IP addresses to use as alternative
subjects of the certificate.</p></li>
<li><p><strong>valid_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Desired number of days for which the new
certificate will be valid.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_venafi.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_dn</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">chain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr_pem</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecdsa_curve</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_hint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pkcs12</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_pem</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_bits</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_dns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_emails</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">san_ips</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_days</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_venafi.Certificate" title="pulumi_venafi.Certificate">Certificate</a><a class="headerlink" href="#pulumi_venafi.Certificate.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key encryption algorithm, either <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">ECDSA</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">RSA</span></code>.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The X509 certificate in PEM format.</p></li>
<li><p><strong>chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The trust chain of X509 certificate authority certificates in PEM format
concatenated together.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common name of the certificate.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>custom_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Collection of Custom Field name-value pairs to
assign to the certificate.</p></li>
<li><p><strong>ecdsa_curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ECDSA curve to use when generating a key</p></li>
<li><p><strong>expiration_window</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of hours before certificate expiry
to request a new certificate.</p></li>
<li><p><strong>issuer_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used with valid_days to indicate the target
issuer when using Trust Protection Platform.  Relevant values are: “DigiCert”,
“Entrust”, and “Microsoft”.</p></li>
<li><p><strong>key_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to encrypt the private key.</p></li>
<li><p><strong>pkcs12</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A base64-encoded PKCS#12 keystore secured by the <code class="docutils literal notranslate"><span class="pre">key_password</span></code>.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key in PEM format.</p></li>
<li><p><strong>rsa_bits</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of bits to use when generating an RSA key.
Applies when <code class="docutils literal notranslate"><span class="pre">algorithm=RSA</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p></li>
<li><p><strong>san_dns</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of DNS names to use as alternative
subjects of the certificate.</p></li>
<li><p><strong>san_emails</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of email addresses to use as
alternative subjects of the certificate.</p></li>
<li><p><strong>san_ips</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of IP addresses to use as alternative
subjects of the certificate.</p></li>
<li><p><strong>valid_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Desired number of days for which the new
certificate will be valid.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_venafi.Certificate.algorithm" title="Permalink to this definition"></a></dt>
<dd><p>Key encryption algorithm, either <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">ECDSA</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">RSA</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_venafi.Certificate.certificate" title="Permalink to this definition"></a></dt>
<dd><p>The X509 certificate in PEM format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.chain">
<em class="property">property </em><code class="sig-name descname">chain</code><a class="headerlink" href="#pulumi_venafi.Certificate.chain" title="Permalink to this definition"></a></dt>
<dd><p>The trust chain of X509 certificate authority certificates in PEM format
concatenated together.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.common_name">
<em class="property">property </em><code class="sig-name descname">common_name</code><a class="headerlink" href="#pulumi_venafi.Certificate.common_name" title="Permalink to this definition"></a></dt>
<dd><p>The common name of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.custom_fields">
<em class="property">property </em><code class="sig-name descname">custom_fields</code><a class="headerlink" href="#pulumi_venafi.Certificate.custom_fields" title="Permalink to this definition"></a></dt>
<dd><p>Collection of Custom Field name-value pairs to
assign to the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.ecdsa_curve">
<em class="property">property </em><code class="sig-name descname">ecdsa_curve</code><a class="headerlink" href="#pulumi_venafi.Certificate.ecdsa_curve" title="Permalink to this definition"></a></dt>
<dd><p>ECDSA curve to use when generating a key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.expiration_window">
<em class="property">property </em><code class="sig-name descname">expiration_window</code><a class="headerlink" href="#pulumi_venafi.Certificate.expiration_window" title="Permalink to this definition"></a></dt>
<dd><p>Number of hours before certificate expiry
to request a new certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.issuer_hint">
<em class="property">property </em><code class="sig-name descname">issuer_hint</code><a class="headerlink" href="#pulumi_venafi.Certificate.issuer_hint" title="Permalink to this definition"></a></dt>
<dd><p>Used with valid_days to indicate the target
issuer when using Trust Protection Platform.  Relevant values are: “DigiCert”,
“Entrust”, and “Microsoft”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.key_password">
<em class="property">property </em><code class="sig-name descname">key_password</code><a class="headerlink" href="#pulumi_venafi.Certificate.key_password" title="Permalink to this definition"></a></dt>
<dd><p>The password used to encrypt the private key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.pkcs12">
<em class="property">property </em><code class="sig-name descname">pkcs12</code><a class="headerlink" href="#pulumi_venafi.Certificate.pkcs12" title="Permalink to this definition"></a></dt>
<dd><p>A base64-encoded PKCS#12 keystore secured by the <code class="docutils literal notranslate"><span class="pre">key_password</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.private_key_pem">
<em class="property">property </em><code class="sig-name descname">private_key_pem</code><a class="headerlink" href="#pulumi_venafi.Certificate.private_key_pem" title="Permalink to this definition"></a></dt>
<dd><p>The private key in PEM format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.rsa_bits">
<em class="property">property </em><code class="sig-name descname">rsa_bits</code><a class="headerlink" href="#pulumi_venafi.Certificate.rsa_bits" title="Permalink to this definition"></a></dt>
<dd><p>Number of bits to use when generating an RSA key.
Applies when <code class="docutils literal notranslate"><span class="pre">algorithm=RSA</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.san_dns">
<em class="property">property </em><code class="sig-name descname">san_dns</code><a class="headerlink" href="#pulumi_venafi.Certificate.san_dns" title="Permalink to this definition"></a></dt>
<dd><p>List of DNS names to use as alternative
subjects of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.san_emails">
<em class="property">property </em><code class="sig-name descname">san_emails</code><a class="headerlink" href="#pulumi_venafi.Certificate.san_emails" title="Permalink to this definition"></a></dt>
<dd><p>List of email addresses to use as
alternative subjects of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.san_ips">
<em class="property">property </em><code class="sig-name descname">san_ips</code><a class="headerlink" href="#pulumi_venafi.Certificate.san_ips" title="Permalink to this definition"></a></dt>
<dd><p>List of IP addresses to use as alternative
subjects of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.valid_days">
<em class="property">property </em><code class="sig-name descname">valid_days</code><a class="headerlink" href="#pulumi_venafi.Certificate.valid_days" title="Permalink to this definition"></a></dt>
<dd><p>Desired number of days for which the new
certificate will be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_venafi.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Certificate.translate_output_property" title="Permalink to this definition"></a></dt>
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

<dl class="py method">
<dt id="pulumi_venafi.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Certificate.translate_input_property" title="Permalink to this definition"></a></dt>
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

<dl class="py class">
<dt id="pulumi_venafi.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_venafi.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dev_mode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tpp_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tpp_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trust_bundle</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the venafi package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access token for TPP, user should use this for authentication</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for Venafi Cloud. Example: 142231b7-cvb0-412e-886b-6aeght0bc93d</p></li>
<li><p><strong>dev_mode</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When set to true, the resulting certificate will be issued by an ephemeral, no trust CA rather than enrolling using
Venafi Cloud or Platform. Useful for development and testing.</p></li>
<li><p><strong>tpp_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for WebSDK user. Example: password</p></li>
<li><p><strong>tpp_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – WebSDK user for Venafi Platform. Example: admin</p></li>
<li><p><strong>trust_bundle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use to specify a PEM-formatted file that contains certificates to be trust anchors for all communications with the
Venafi Web Service. Example: trust_bundle = “${file(“chain.pem”)}”</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Venafi Web Service URL.. Example: <a class="reference external" href="https://tpp.venafi.example/vedsdk">https://tpp.venafi.example/vedsdk</a></p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DN of the Venafi Platform policy folder or name of the Venafi Cloud zone. Example for Platform: testpolicyvault
Example for Venafi Cloud: Default</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_venafi.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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

<dl class="py method">
<dt id="pulumi_venafi.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_venafi.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
