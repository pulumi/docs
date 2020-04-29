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
<span class="target" id="module-pulumi_gcp.binaryauthorization"></span><dl class="class">
<dt id="pulumi_gcp.binaryauthorization.Attestor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">Attestor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestation_authority_note=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.attestation_authority_note">
<code class="sig-name descname">attestation_authority_note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.attestation_authority_note" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment. This field may be updated. The field may be
displayed in chooser dialogs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Attestor.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestation_authority_note=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.attestor">
<code class="sig-name descname">attestor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.attestor">
<code class="sig-name descname">attestor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">binaryauthorization.AttestorIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">AttestorIamPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.attestor">
<code class="sig-name descname">attestor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestor=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.AttestorIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.binaryauthorization.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admission_whitelist_patterns=None</em>, <em class="sig-param">cluster_admission_rules=None</em>, <em class="sig-param">default_admission_rule=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">global_policy_evaluation_mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.admission_whitelist_patterns">
<code class="sig-name descname">admission_whitelist_patterns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.admission_whitelist_patterns" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.cluster_admission_rules">
<code class="sig-name descname">cluster_admission_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.cluster_admission_rules" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.default_admission_rule">
<code class="sig-name descname">default_admission_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.default_admission_rule" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.global_policy_evaluation_mode">
<code class="sig-name descname">global_policy_evaluation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.global_policy_evaluation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls the evaluation of a Google-maintained global admission policy
for common system-level images. Images not covered by the global
policy will be subject to the project admission policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.binaryauthorization.Policy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admission_whitelist_patterns=None</em>, <em class="sig-param">cluster_admission_rules=None</em>, <em class="sig-param">default_admission_rule=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">global_policy_evaluation_mode=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
