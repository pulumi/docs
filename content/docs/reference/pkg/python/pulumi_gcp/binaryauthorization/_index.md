---
title: Module binaryauthorization
title_tag: Module binaryauthorization | Package pulumi_gcp | Python SDK
linktitle: binaryauthorization
notitle: true
---

<div class="section" id="binaryauthorization">
<h1>binaryauthorization<a class="headerlink" href="#binaryauthorization" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.binaryauthorization"></span><dl class="py class">
<dt id="pulumi_gcp.binaryauthorization.Attestor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">Attestor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation_authority_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>An attestor that attests to container image artifacts.</p>
<p>To get more information about Attestor, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/docs/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">note</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">containeranalysis</span><span class="o">.</span><span class="n">Note</span><span class="p">(</span><span class="s2">&quot;note&quot;</span><span class="p">,</span> <span class="n">attestation_authority</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;hint&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;humanReadableName&quot;</span><span class="p">:</span> <span class="s2">&quot;Attestor Note&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">})</span>
<span class="n">attestor</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">Attestor</span><span class="p">(</span><span class="s2">&quot;attestor&quot;</span><span class="p">,</span> <span class="n">attestation_authority_note</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;noteReference&quot;</span><span class="p">:</span> <span class="n">note</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="s2">&quot;public_keys&quot;</span><span class="p">:</span> <span class="p">[{</span>
        <span class="s2">&quot;asciiArmoredPgpPublicKey&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;mQENBFtP0doBCADF+joTiXWKVuP8kJt3fgpBSjT9h8ezMfKA4aXZctYLx5wslWQl</span>
<span class="s2">bB7Iu2ezkECNzoEeU7WxUe8a61pMCh9cisS9H5mB2K2uM4Jnf8tgFeXn3akJDVo0</span>
<span class="s2">oR1IC+Dp9mXbRSK3MAvKkOwWlG99sx3uEdvmeBRHBOO+grchLx24EThXFOyP9Fk6</span>
<span class="s2">V39j6xMjw4aggLD15B4V0v9JqBDdJiIYFzszZDL6pJwZrzcP0z8JO4rTZd+f64bD</span>
<span class="s2">Mpj52j/pQfA8lZHOaAgb1OrthLdMrBAjoDjArV4Ek7vSbrcgYWcI6BhsQrFoxKdX</span>
<span class="s2">83TZKai55ZCfCLIskwUIzA1NLVwyzCS+fSN/ABEBAAG0KCJUZXN0IEF0dGVzdG9y</span>
<span class="s2">IiA8ZGFuYWhvZmZtYW5AZ29vZ2xlLmNvbT6JAU4EEwEIADgWIQRfWkqHt6hpTA1L</span>
<span class="s2">uY060eeM4dc66AUCW0/R2gIbLwULCQgHAgYVCgkICwIEFgIDAQIeAQIXgAAKCRA6</span>
<span class="s2">0eeM4dc66HdpCAC4ot3b0OyxPb0Ip+WT2U0PbpTBPJklesuwpIrM4Lh0N+1nVRLC</span>
<span class="s2">51WSmVbM8BiAFhLbN9LpdHhds1kUrHF7+wWAjdR8sqAj9otc6HGRM/3qfa2qgh+U</span>
<span class="s2">WTEk/3us/rYSi7T7TkMuutRMIa1IkR13uKiW56csEMnbOQpn9rDqwIr5R8nlZP5h</span>
<span class="s2">MAU9vdm1DIv567meMqTaVZgR3w7bck2P49AO8lO5ERFpVkErtu/98y+rUy9d789l</span>
<span class="s2">+OPuS1NGnxI1YKsNaWJF4uJVuvQuZ1twrhCbGNtVorO2U12+cEq+YtUxj7kmdOC1</span>
<span class="s2">qoIRW6y0+UlAc+MbqfL0ziHDOAmcqz1GnROg</span>
<span class="s2">=6Bvm</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
<span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestation_authority_note</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment. This field may be updated. The field may be
displayed in chooser dialogs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation_authority_note</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delegationServiceAccountEmail</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
This field will contain the service account email address that
this Attestor will use as the principal when querying Container
Analysis. Attestor administrators must grant this service account
the IAM role needed to read attestations from the noteReference in
Container Analysis (containeranalysis.notes.occurrences.viewer).
This email address is fixed for the lifetime of the Attestor, but
callers should not make any other assumptions about the service
account email; future versions may use an email based on a
different naming pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">noteReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource name of a ATTESTATION_AUTHORITY Note, created by the
user. If the Note is in a different project from the Attestor, it
should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/notes/*</span></code> (or the legacy
<code class="docutils literal notranslate"><span class="pre">providers/*/notes/*</span></code>). This field may not be updated.
An attestation by this attestor is stored as a Container Analysis
ATTESTATION_AUTHORITY Occurrence that names a container image
and that links to this Note.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Public keys that verify attestations signed by this attestor. This
field may be updated.
If this field is non-empty, one of the specified public keys must
verify that an attestation was signed by this attestor for the
image specified in the admission request.
If this field is empty, this attestor always returns that no valid
attestations exist.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">asciiArmoredPgpPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ASCII-armored representation of a PGP public key, as the
entire output by the command
<code class="docutils literal notranslate"><span class="pre">gpg</span> <span class="pre">--export</span> <span class="pre">--armor</span> <span class="pre">foo&#64;example.com</span></code> (either LF or CRLF
line endings). When using this field, id should be left
blank. The BinAuthz API handlers will calculate the ID
and fill it in automatically. BinAuthz computes this ID
as the OpenPGP RFC4880 V4 fingerprint, represented as
upper-case hex. If id is provided by the caller, it will
be overwritten by the API-calculated ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A descriptive comment. This field may be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this public key. Signatures verified by BinAuthz
must include the ID of the public key that can be used to
verify them, and that ID must match the contents of this
field exactly. Additional restrictions on this field can
be imposed based on which public key type is encapsulated.
See the documentation on publicKey cases below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pkixPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A raw PKIX SubjectPublicKeyInfo format public key.
NOTE: id may be explicitly provided by the caller when using this
type of public key, but it MUST be a valid RFC3986 URI. If id is left
blank, a default one will be computed based on the digest of the DER
encoding of the public key.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyPem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A PEM-encoded public key, as described in
<code class="docutils literal notranslate"><span class="pre">https://tools.ietf.org/html/rfc7468#section-13</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The signature algorithm used to verify a message against
a signature using this key. These signature algorithm must
match the structure and any object identifiers encoded in
publicKeyPem (i.e. this algorithm must match that of the
public key).</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.attestation_authority_note">
<code class="sig-name descname">attestation_authority_note</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.attestation_authority_note" title="Permalink to this definition">¶</a></dt>
<dd><p>A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delegationServiceAccountEmail</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
This field will contain the service account email address that
this Attestor will use as the principal when querying Container
Analysis. Attestor administrators must grant this service account
the IAM role needed to read attestations from the noteReference in
Container Analysis (containeranalysis.notes.occurrences.viewer).
This email address is fixed for the lifetime of the Attestor, but
callers should not make any other assumptions about the service
account email; future versions may use an email based on a
different naming pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">noteReference</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource name of a ATTESTATION_AUTHORITY Note, created by the
user. If the Note is in a different project from the Attestor, it
should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/notes/*</span></code> (or the legacy
<code class="docutils literal notranslate"><span class="pre">providers/*/notes/*</span></code>). This field may not be updated.
An attestation by this attestor is stored as a Container Analysis
ATTESTATION_AUTHORITY Occurrence that names a container image
and that links to this Note.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Public keys that verify attestations signed by this attestor. This
field may be updated.
If this field is non-empty, one of the specified public keys must
verify that an attestation was signed by this attestor for the
image specified in the admission request.
If this field is empty, this attestor always returns that no valid
attestations exist.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">asciiArmoredPgpPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ASCII-armored representation of a PGP public key, as the
entire output by the command
<code class="docutils literal notranslate"><span class="pre">gpg</span> <span class="pre">--export</span> <span class="pre">--armor</span> <span class="pre">foo&#64;example.com</span></code> (either LF or CRLF
line endings). When using this field, id should be left
blank. The BinAuthz API handlers will calculate the ID
and fill it in automatically. BinAuthz computes this ID
as the OpenPGP RFC4880 V4 fingerprint, represented as
upper-case hex. If id is provided by the caller, it will
be overwritten by the API-calculated ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A descriptive comment. This field may be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of this public key. Signatures verified by BinAuthz
must include the ID of the public key that can be used to
verify them, and that ID must match the contents of this
field exactly. Additional restrictions on this field can
be imposed based on which public key type is encapsulated.
See the documentation on publicKey cases below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pkixPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A raw PKIX SubjectPublicKeyInfo format public key.
NOTE: id may be explicitly provided by the caller when using this
type of public key, but it MUST be a valid RFC3986 URI. If id is left
blank, a default one will be computed based on the digest of the DER
encoding of the public key.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyPem</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A PEM-encoded public key, as described in
<code class="docutils literal notranslate"><span class="pre">https://tools.ietf.org/html/rfc7468#section-13</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The signature algorithm used to verify a message against
a signature using this key. These signature algorithm must
match the structure and any object identifiers encoded in
publicKeyPem (i.e. this algorithm must match that of the
public key).</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment. This field may be updated. The field may be
displayed in chooser dialogs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation_authority_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Attestor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestation_authority_note</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment. This field may be updated. The field may be
displayed in chooser dialogs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation_authority_note</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delegationServiceAccountEmail</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
This field will contain the service account email address that
this Attestor will use as the principal when querying Container
Analysis. Attestor administrators must grant this service account
the IAM role needed to read attestations from the noteReference in
Container Analysis (containeranalysis.notes.occurrences.viewer).
This email address is fixed for the lifetime of the Attestor, but
callers should not make any other assumptions about the service
account email; future versions may use an email based on a
different naming pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">noteReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource name of a ATTESTATION_AUTHORITY Note, created by the
user. If the Note is in a different project from the Attestor, it
should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/notes/*</span></code> (or the legacy
<code class="docutils literal notranslate"><span class="pre">providers/*/notes/*</span></code>). This field may not be updated.
An attestation by this attestor is stored as a Container Analysis
ATTESTATION_AUTHORITY Occurrence that names a container image
and that links to this Note.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Public keys that verify attestations signed by this attestor. This
field may be updated.
If this field is non-empty, one of the specified public keys must
verify that an attestation was signed by this attestor for the
image specified in the admission request.
If this field is empty, this attestor always returns that no valid
attestations exist.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">asciiArmoredPgpPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ASCII-armored representation of a PGP public key, as the
entire output by the command
<code class="docutils literal notranslate"><span class="pre">gpg</span> <span class="pre">--export</span> <span class="pre">--armor</span> <span class="pre">foo&#64;example.com</span></code> (either LF or CRLF
line endings). When using this field, id should be left
blank. The BinAuthz API handlers will calculate the ID
and fill it in automatically. BinAuthz computes this ID
as the OpenPGP RFC4880 V4 fingerprint, represented as
upper-case hex. If id is provided by the caller, it will
be overwritten by the API-calculated ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A descriptive comment. This field may be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this public key. Signatures verified by BinAuthz
must include the ID of the public key that can be used to
verify them, and that ID must match the contents of this
field exactly. Additional restrictions on this field can
be imposed based on which public key type is encapsulated.
See the documentation on publicKey cases below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pkixPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A raw PKIX SubjectPublicKeyInfo format public key.
NOTE: id may be explicitly provided by the caller when using this
type of public key, but it MUST be a valid RFC3986 URI. If id is left
blank, a default one will be computed based on the digest of the DER
encoding of the public key.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyPem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A PEM-encoded public key, as described in
<code class="docutils literal notranslate"><span class="pre">https://tools.ietf.org/html/rfc7468#section-13</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The signature algorithm used to verify a message against
a signature using this key. These signature algorithm must
match the structure and any object identifiers encoded in
publicKeyPem (i.e. this algorithm must match that of the
public key).</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Binary Authorization Attestor. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code>: Authoritative. Sets the IAM policy for the attestor and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the attestor are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the attestor are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.attestor">
<code class="sig-name descname">attestor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttestorIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Binary Authorization Attestor. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code>: Authoritative. Sets the IAM policy for the attestor and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the attestor are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the attestor are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.attestor">
<code class="sig-name descname">attestor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttestorIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Binary Authorization Attestor. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code>: Authoritative. Sets the IAM policy for the attestor and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the attestor are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the attestor are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">AttestorIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">attestor</span><span class="o">=</span><span class="n">google_binary_authorization_attestor</span><span class="p">[</span><span class="s2">&quot;attestor&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.attestor">
<code class="sig-name descname">attestor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttestorIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admission_whitelist_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_admission_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_admission_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_policy_evaluation_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy for container image binary authorization.</p>
<p>To get more information about Policy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/docs/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">note</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">containeranalysis</span><span class="o">.</span><span class="n">Note</span><span class="p">(</span><span class="s2">&quot;note&quot;</span><span class="p">,</span> <span class="n">attestation_authority</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;hint&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;humanReadableName&quot;</span><span class="p">:</span> <span class="s2">&quot;My attestor&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">})</span>
<span class="n">attestor</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">Attestor</span><span class="p">(</span><span class="s2">&quot;attestor&quot;</span><span class="p">,</span> <span class="n">attestation_authority_note</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;noteReference&quot;</span><span class="p">:</span> <span class="n">note</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
<span class="p">})</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">admission_whitelist_patterns</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;namePattern&quot;</span><span class="p">:</span> <span class="s2">&quot;gcr.io/google_containers/*&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">default_admission_rule</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;evaluationMode&quot;</span><span class="p">:</span> <span class="s2">&quot;ALWAYS_ALLOW&quot;</span><span class="p">,</span>
        <span class="s2">&quot;enforcementMode&quot;</span><span class="p">:</span> <span class="s2">&quot;ENFORCED_BLOCK_AND_AUDIT_LOG&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">cluster_admission_rules</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;cluster&quot;</span><span class="p">:</span> <span class="s2">&quot;us-central1-a.prod-cluster&quot;</span><span class="p">,</span>
        <span class="s2">&quot;evaluationMode&quot;</span><span class="p">:</span> <span class="s2">&quot;REQUIRE_ATTESTATION&quot;</span><span class="p">,</span>
        <span class="s2">&quot;enforcementMode&quot;</span><span class="p">:</span> <span class="s2">&quot;ENFORCED_BLOCK_AND_AUDIT_LOG&quot;</span><span class="p">,</span>
        <span class="s2">&quot;requireAttestationsBies&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">attestor</span><span class="o">.</span><span class="n">name</span><span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">note</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">containeranalysis</span><span class="o">.</span><span class="n">Note</span><span class="p">(</span><span class="s2">&quot;note&quot;</span><span class="p">,</span> <span class="n">attestation_authority</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;hint&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;humanReadableName&quot;</span><span class="p">:</span> <span class="s2">&quot;My attestor&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">})</span>
<span class="n">attestor</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">Attestor</span><span class="p">(</span><span class="s2">&quot;attestor&quot;</span><span class="p">,</span> <span class="n">attestation_authority_note</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;noteReference&quot;</span><span class="p">:</span> <span class="n">note</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
<span class="p">})</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">binaryauthorization</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">default_admission_rule</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;evaluationMode&quot;</span><span class="p">:</span> <span class="s2">&quot;REQUIRE_ATTESTATION&quot;</span><span class="p">,</span>
        <span class="s2">&quot;enforcementMode&quot;</span><span class="p">:</span> <span class="s2">&quot;ENFORCED_BLOCK_AND_AUDIT_LOG&quot;</span><span class="p">,</span>
        <span class="s2">&quot;requireAttestationsBies&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">attestor</span><span class="o">.</span><span class="n">name</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="n">global_policy_evaluation_mode</span><span class="o">=</span><span class="s2">&quot;ENABLE&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admission_whitelist_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A whitelist of image patterns to exclude from admission rules. If an
image’s name matches a whitelist pattern, the image’s admission
requests will always be permitted regardless of your admission rules.  Structure is documented below.</p></li>
<li><p><strong>cluster_admission_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Per-cluster admission rules. An admission rule specifies either that
all container images used in a pod creation request must be attested
to by one or more attestors, that all pod creations will be allowed,
or that all pod creations will be denied. There can be at most one
admission rule per cluster spec.</p></li>
<li><p><strong>default_admission_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default admission rule for a cluster without a per-cluster admission
rule.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment.</p></li>
<li><p><strong>global_policy_evaluation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls the evaluation of a Google-maintained global admission policy
for common system-level images. Images not covered by the global
policy will be subject to the project admission policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>admission_whitelist_patterns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An image name pattern to whitelist, in the form
<code class="docutils literal notranslate"><span class="pre">registry/path/to/image</span></code>. This supports a trailing * as a
wildcard, but this is allowed only in text after the registry/
part.</p></li>
</ul>
<p>The <strong>cluster_admission_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
<p>The <strong>default_admission_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.admission_whitelist_patterns">
<code class="sig-name descname">admission_whitelist_patterns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.admission_whitelist_patterns" title="Permalink to this definition">¶</a></dt>
<dd><p>A whitelist of image patterns to exclude from admission rules. If an
image’s name matches a whitelist pattern, the image’s admission
requests will always be permitted regardless of your admission rules.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An image name pattern to whitelist, in the form
<code class="docutils literal notranslate"><span class="pre">registry/path/to/image</span></code>. This supports a trailing * as a
wildcard, but this is allowed only in text after the registry/
part.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.cluster_admission_rules">
<code class="sig-name descname">cluster_admission_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.cluster_admission_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Per-cluster admission rules. An admission rule specifies either that
all container images used in a pod creation request must be attested
to by one or more attestors, that all pod creations will be allowed,
or that all pod creations will be denied. There can be at most one
admission rule per cluster spec.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.default_admission_rule">
<code class="sig-name descname">default_admission_rule</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.default_admission_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Default admission rule for a cluster without a per-cluster admission
rule.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.global_policy_evaluation_mode">
<code class="sig-name descname">global_policy_evaluation_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.global_policy_evaluation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls the evaluation of a Google-maintained global admission policy
for common system-level images. Images not covered by the global
policy will be subject to the project admission policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admission_whitelist_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_admission_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_admission_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_policy_evaluation_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admission_whitelist_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A whitelist of image patterns to exclude from admission rules. If an
image’s name matches a whitelist pattern, the image’s admission
requests will always be permitted regardless of your admission rules.  Structure is documented below.</p></li>
<li><p><strong>cluster_admission_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Per-cluster admission rules. An admission rule specifies either that
all container images used in a pod creation request must be attested
to by one or more attestors, that all pod creations will be allowed,
or that all pod creations will be denied. There can be at most one
admission rule per cluster spec.</p></li>
<li><p><strong>default_admission_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default admission rule for a cluster without a per-cluster admission
rule.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment.</p></li>
<li><p><strong>global_policy_evaluation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls the evaluation of a Google-maintained global admission policy
for common system-level images. Images not covered by the global
policy will be subject to the project admission policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>admission_whitelist_patterns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An image name pattern to whitelist, in the form
<code class="docutils literal notranslate"><span class="pre">registry/path/to/image</span></code>. This supports a trailing * as a
wildcard, but this is allowed only in text after the registry/
part.</p></li>
</ul>
<p>The <strong>cluster_admission_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
<p>The <strong>default_admission_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action when a pod creation is denied by the admission rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How this admission rule will be evaluated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAttestationsBies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The resource names of the attestors that must attest to a
container image. If the attestor is in a different project from the
policy, it should be specified in the format <code class="docutils literal notranslate"><span class="pre">projects/*/attestors/*</span></code>.
Each attestor must exist before a policy can reference it. To add an
attestor to a policy the principal issuing the policy change
request must be able to read the attestor resource.
Note: this field must be non-empty when the evaluation_mode field
specifies REQUIRE_ATTESTATION, otherwise it must be empty.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
