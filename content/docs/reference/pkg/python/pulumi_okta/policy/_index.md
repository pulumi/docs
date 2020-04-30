---
title: Module policy
title_tag: Module policy | Package pulumi_okta | Python SDK
linktitle: policy
notitle: true
---

<div class="section" id="policy">
<h1>policy<a class="headerlink" href="#policy" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.policy"></span><dl class="py class">
<dt id="pulumi_okta.policy.AwaitableGetDefaultPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">AwaitableGetDefaultPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.AwaitableGetDefaultPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_okta.policy.AwaitableGetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">AwaitableGetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.AwaitableGetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_okta.policy.GetDefaultPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">GetDefaultPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.GetDefaultPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultPolicy.</p>
<dl class="py attribute">
<dt id="pulumi_okta.policy.GetDefaultPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.GetDefaultPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.GetDefaultPolicyResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.GetDefaultPolicyResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>type of policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_okta.policy.GetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">GetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="py attribute">
<dt id="pulumi_okta.policy.GetPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.GetPolicyResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.GetPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.GetPolicyResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.GetPolicyResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>type of policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_okta.policy.Mfa">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">Mfa</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_u2f</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_webauthn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_call</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_push</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_question</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_sms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">symantec_vip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">yubikey_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Mfa" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an MFA Policy.</p>
<p>This resource allows you to create and configure an MFA Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>duo</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DUO MFA policy settings.</p></li>
<li><p><strong>fido_u2f</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Fido U2F MFA policy settings.</p></li>
<li><p><strong>fido_webauthn</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Fido Web Authn MFA policy settings.</p></li>
<li><p><strong>google_otp</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Google OTP MFA policy settings.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>okta_call</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Call MFA policy settings.</p></li>
<li><p><strong>okta_otp</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta OTP MFA policy settings.</p></li>
<li><p><strong>okta_password</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Password MFA policy settings.</p></li>
<li><p><strong>okta_push</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Push MFA policy settings.</p></li>
<li><p><strong>okta_question</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Question MFA policy settings.</p></li>
<li><p><strong>okta_sms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta SMS MFA policy settings.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>rsa_token</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – RSA Token MFA policy settings.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>symantec_vip</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Symantec VIP MFA policy settings.</p></li>
<li><p><strong>yubikey_token</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Yubikey Token MFA policy settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.duo">
<code class="sig-name descname">duo</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.duo" title="Permalink to this definition">¶</a></dt>
<dd><p>DUO MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.fido_u2f">
<code class="sig-name descname">fido_u2f</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.fido_u2f" title="Permalink to this definition">¶</a></dt>
<dd><p>Fido U2F MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.fido_webauthn">
<code class="sig-name descname">fido_webauthn</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.fido_webauthn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fido Web Authn MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.google_otp">
<code class="sig-name descname">google_otp</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.google_otp" title="Permalink to this definition">¶</a></dt>
<dd><p>Google OTP MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_call">
<code class="sig-name descname">okta_call</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_call" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta Call MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_otp">
<code class="sig-name descname">okta_otp</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_otp" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta OTP MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_password">
<code class="sig-name descname">okta_password</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta Password MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_push">
<code class="sig-name descname">okta_push</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_push" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta Push MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_question">
<code class="sig-name descname">okta_question</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_question" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta Question MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.okta_sms">
<code class="sig-name descname">okta_sms</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.okta_sms" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta SMS MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.rsa_token">
<code class="sig-name descname">rsa_token</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.rsa_token" title="Permalink to this definition">¶</a></dt>
<dd><p>RSA Token MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.symantec_vip">
<code class="sig-name descname">symantec_vip</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.symantec_vip" title="Permalink to this definition">¶</a></dt>
<dd><p>Symantec VIP MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Mfa.yubikey_token">
<code class="sig-name descname">yubikey_token</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Mfa.yubikey_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Yubikey Token MFA policy settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Mfa.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_u2f</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_webauthn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_call</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_push</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_question</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_sms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">symantec_vip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">yubikey_token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Mfa.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Mfa resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>duo</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DUO MFA policy settings.</p></li>
<li><p><strong>fido_u2f</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Fido U2F MFA policy settings.</p></li>
<li><p><strong>fido_webauthn</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Fido Web Authn MFA policy settings.</p></li>
<li><p><strong>google_otp</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Google OTP MFA policy settings.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>okta_call</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Call MFA policy settings.</p></li>
<li><p><strong>okta_otp</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta OTP MFA policy settings.</p></li>
<li><p><strong>okta_password</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Password MFA policy settings.</p></li>
<li><p><strong>okta_push</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Push MFA policy settings.</p></li>
<li><p><strong>okta_question</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta Question MFA policy settings.</p></li>
<li><p><strong>okta_sms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Okta SMS MFA policy settings.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>rsa_token</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – RSA Token MFA policy settings.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>symantec_vip</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Symantec VIP MFA policy settings.</p></li>
<li><p><strong>yubikey_token</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Yubikey Token MFA policy settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User consent type required before enrolling in the factor: <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;TERMS_OF_SERVICE&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Requirements for user initiated enrollment. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NOT_ALLOWED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;OPTIONAL&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Mfa.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Mfa.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.Mfa.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Mfa.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.Password">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">Password</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_auto_unlock_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_dictionary_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_expire_warn_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_history_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_age_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_lockout_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_age_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_lowercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_symbol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_uppercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_show_lockout_failures</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_email_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Password" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Password Policy.</p>
<p>This resource allows you to create and configure a Password Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication Provider: <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE_DIRECTORY&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>email_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable email password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>password_auto_unlock_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of minutes before a locked account is unlocked: 0 = no limit.</p></li>
<li><p><strong>password_dictionary_lookup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Check Passwords Against Common Password Dictionary.</p></li>
<li><p><strong>password_exclude_first_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User firstName attribute must be excluded from the password.</p></li>
<li><p><strong>password_exclude_last_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User lastName attribute must be excluded from the password.</p></li>
<li><p><strong>password_exclude_username</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the user name must be excluded from the password.</p></li>
<li><p><strong>password_expire_warn_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a user will be warned before password expiry: 0 = no warning.</p></li>
<li><p><strong>password_history_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of distinct passwords that must be created before they can be reused: 0 = none.</p></li>
<li><p><strong>password_max_age_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a password is valid before expiry: 0 = no limit.”,</p></li>
<li><p><strong>password_max_lockout_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of unsuccessful login attempts allowed before lockout: 0 = no limit.</p></li>
<li><p><strong>password_min_age_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum time interval in minutes between password changes: 0 = no limit.</p></li>
<li><p><strong>password_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum password length. Default is 8.</p></li>
<li><p><strong>password_min_lowercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of lower case characters in password.</p></li>
<li><p><strong>password_min_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of numbers in password.</p></li>
<li><p><strong>password_min_symbol</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of symbols in password.</p></li>
<li><p><strong>password_min_uppercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of upper case characters in password.</p></li>
<li><p><strong>password_show_lockout_failures</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If a user should be informed when their account is locked.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>question_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Min length of the password recovery question answer.</p></li>
<li><p><strong>question_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable security question password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>recovery_email_token</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime in minutes of the recovery email token.</p></li>
<li><p><strong>skip_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s Windows account.</p></li>
<li><p><strong>sms_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.auth_provider">
<code class="sig-name descname">auth_provider</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.auth_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication Provider: <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE_DIRECTORY&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.email_recovery">
<code class="sig-name descname">email_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.email_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable email password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_auto_unlock_minutes">
<code class="sig-name descname">password_auto_unlock_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_auto_unlock_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of minutes before a locked account is unlocked: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_dictionary_lookup">
<code class="sig-name descname">password_dictionary_lookup</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_dictionary_lookup" title="Permalink to this definition">¶</a></dt>
<dd><p>Check Passwords Against Common Password Dictionary.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_exclude_first_name">
<code class="sig-name descname">password_exclude_first_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_exclude_first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User firstName attribute must be excluded from the password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_exclude_last_name">
<code class="sig-name descname">password_exclude_last_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_exclude_last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User lastName attribute must be excluded from the password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_exclude_username">
<code class="sig-name descname">password_exclude_username</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_exclude_username" title="Permalink to this definition">¶</a></dt>
<dd><p>If the user name must be excluded from the password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_expire_warn_days">
<code class="sig-name descname">password_expire_warn_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_expire_warn_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length in days a user will be warned before password expiry: 0 = no warning.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_history_count">
<code class="sig-name descname">password_history_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_history_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of distinct passwords that must be created before they can be reused: 0 = none.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_max_age_days">
<code class="sig-name descname">password_max_age_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_max_age_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length in days a password is valid before expiry: 0 = no limit.”,</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_max_lockout_attempts">
<code class="sig-name descname">password_max_lockout_attempts</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_max_lockout_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of unsuccessful login attempts allowed before lockout: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_age_minutes">
<code class="sig-name descname">password_min_age_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_age_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum time interval in minutes between password changes: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_length">
<code class="sig-name descname">password_min_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum password length. Default is 8.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_lowercase">
<code class="sig-name descname">password_min_lowercase</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_lowercase" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of lower case characters in password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_number">
<code class="sig-name descname">password_min_number</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_number" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of numbers in password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_symbol">
<code class="sig-name descname">password_min_symbol</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_symbol" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of symbols in password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_min_uppercase">
<code class="sig-name descname">password_min_uppercase</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_min_uppercase" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of upper case characters in password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.password_show_lockout_failures">
<code class="sig-name descname">password_show_lockout_failures</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.password_show_lockout_failures" title="Permalink to this definition">¶</a></dt>
<dd><p>If a user should be informed when their account is locked.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.question_min_length">
<code class="sig-name descname">question_min_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.question_min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Min length of the password recovery question answer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.question_recovery">
<code class="sig-name descname">question_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.question_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable security question password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.recovery_email_token">
<code class="sig-name descname">recovery_email_token</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.recovery_email_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Lifetime in minutes of the recovery email token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.skip_unlock">
<code class="sig-name descname">skip_unlock</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.skip_unlock" title="Permalink to this definition">¶</a></dt>
<dd><p>When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s Windows account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.sms_recovery">
<code class="sig-name descname">sms_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.sms_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Password.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Password.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Password.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_auto_unlock_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_dictionary_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_expire_warn_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_history_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_age_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_lockout_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_age_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_lowercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_symbol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_uppercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_show_lockout_failures</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_email_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Password.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Password resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication Provider: <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE_DIRECTORY&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>email_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable email password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>password_auto_unlock_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of minutes before a locked account is unlocked: 0 = no limit.</p></li>
<li><p><strong>password_dictionary_lookup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Check Passwords Against Common Password Dictionary.</p></li>
<li><p><strong>password_exclude_first_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User firstName attribute must be excluded from the password.</p></li>
<li><p><strong>password_exclude_last_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User lastName attribute must be excluded from the password.</p></li>
<li><p><strong>password_exclude_username</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the user name must be excluded from the password.</p></li>
<li><p><strong>password_expire_warn_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a user will be warned before password expiry: 0 = no warning.</p></li>
<li><p><strong>password_history_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of distinct passwords that must be created before they can be reused: 0 = none.</p></li>
<li><p><strong>password_max_age_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a password is valid before expiry: 0 = no limit.”,</p></li>
<li><p><strong>password_max_lockout_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of unsuccessful login attempts allowed before lockout: 0 = no limit.</p></li>
<li><p><strong>password_min_age_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum time interval in minutes between password changes: 0 = no limit.</p></li>
<li><p><strong>password_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum password length. Default is 8.</p></li>
<li><p><strong>password_min_lowercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of lower case characters in password.</p></li>
<li><p><strong>password_min_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of numbers in password.</p></li>
<li><p><strong>password_min_symbol</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of symbols in password.</p></li>
<li><p><strong>password_min_uppercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of upper case characters in password.</p></li>
<li><p><strong>password_show_lockout_failures</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If a user should be informed when their account is locked.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>question_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Min length of the password recovery question answer.</p></li>
<li><p><strong>question_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable security question password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>recovery_email_token</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime in minutes of the recovery email token.</p></li>
<li><p><strong>skip_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s Windows account.</p></li>
<li><p><strong>sms_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Password.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Password.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.Password.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Password.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleIdpDiscovery">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">RuleIdpDiscovery</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an IdP Discovery Policy Rule.</p>
<p>This resource allows you to create and configure an IdP Discovery Policy Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Applications to exclude in discovery rule</p></li>
<li><p><strong>app_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Applications to include in discovery rule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>app_includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>platform_includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">osExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>user_identifier_patterns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">match_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.app_excludes">
<code class="sig-name descname">app_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.app_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>Applications to exclude in discovery rule</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.app_includes">
<code class="sig-name descname">app_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.app_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Applications to include in discovery rule</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_identifier_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleIdpDiscovery resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Applications to exclude in discovery rule</p></li>
<li><p><strong>app_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Applications to include in discovery rule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>app_includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Policy Rule Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>platform_includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">osExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>user_identifier_patterns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">match_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleIdpDiscovery.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleIdpDiscovery.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleIdpDiscovery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleMfa">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">RuleMfa</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enroll</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleMfa" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an MFA Policy Rule.</p>
<p>This resource allows you to create and configure an MFA Policy Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enroll</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When a user should be prompted for MFA. It can be <code class="docutils literal notranslate"><span class="pre">&quot;CHALLENGE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LOGIN&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;NEVER&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.enroll">
<code class="sig-name descname">enroll</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.enroll" title="Permalink to this definition">¶</a></dt>
<dd><p>When a user should be prompted for MFA. It can be <code class="docutils literal notranslate"><span class="pre">&quot;CHALLENGE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LOGIN&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;NEVER&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleMfa.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleMfa.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enroll</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleMfa resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enroll</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When a user should be prompted for MFA. It can be <code class="docutils literal notranslate"><span class="pre">&quot;CHALLENGE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LOGIN&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;NEVER&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleMfa.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleMfa.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleMfa.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RulePassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">RulePassword</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_change</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RulePassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Password Policy Rule.</p>
<p>This resource allows you to create and configure a Password Policy Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>password_change</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to change their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>password_reset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to reset their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>password_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to unlock: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>,</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.password_change">
<code class="sig-name descname">password_change</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.password_change" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to change their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.password_reset">
<code class="sig-name descname">password_reset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.password_reset" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to reset their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.password_unlock">
<code class="sig-name descname">password_unlock</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.password_unlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to unlock: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>,</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RulePassword.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RulePassword.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RulePassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_change</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RulePassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RulePassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>password_change</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to change their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>password_reset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to reset their password: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>password_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to unlock: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>,</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RulePassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RulePassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RulePassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RulePassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleSignon">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">RuleSignon</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authtype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_prompt</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_remember_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_idle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_persistent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleSignon" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Sign On Policy Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny access based on the rule conditions: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>authtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication entrypoint: <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;RADIUS&quot;</span></code>.</p></li>
<li><p><strong>mfa_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Elapsed time before the next MFA challenge.</p></li>
<li><p><strong>mfa_prompt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: <code class="docutils literal notranslate"><span class="pre">&quot;DEVICE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ALWAYS&quot;</span></code>.</p></li>
<li><p><strong>mfa_remember_device</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Remember MFA device. The default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>mfa_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Require MFA. By default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>session_idle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session can be idle.”,</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session is active: Disable = 0.</p></li>
<li><p><strong>session_persistent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.access">
<code class="sig-name descname">access</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.access" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny access based on the rule conditions: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.authtype">
<code class="sig-name descname">authtype</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.authtype" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication entrypoint: <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;RADIUS&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.mfa_lifetime">
<code class="sig-name descname">mfa_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.mfa_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Elapsed time before the next MFA challenge.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.mfa_prompt">
<code class="sig-name descname">mfa_prompt</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.mfa_prompt" title="Permalink to this definition">¶</a></dt>
<dd><p>Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: <code class="docutils literal notranslate"><span class="pre">&quot;DEVICE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ALWAYS&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.mfa_remember_device">
<code class="sig-name descname">mfa_remember_device</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.mfa_remember_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Remember MFA device. The default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.mfa_required">
<code class="sig-name descname">mfa_required</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.mfa_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Require MFA. By default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.session_idle">
<code class="sig-name descname">session_idle</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.session_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>Max minutes a session can be idle.”,</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.session_lifetime">
<code class="sig-name descname">session_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.session_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Max minutes a session is active: Disable = 0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.session_persistent">
<code class="sig-name descname">session_persistent</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.session_persistent" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.RuleSignon.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleSignon.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authtype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_prompt</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_remember_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_idle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_persistent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleSignon resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny access based on the rule conditions: <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;DENY&quot;</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">&quot;ALLOW&quot;</span></code>.</p></li>
<li><p><strong>authtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication entrypoint: <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;RADIUS&quot;</span></code>.</p></li>
<li><p><strong>mfa_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Elapsed time before the next MFA challenge.</p></li>
<li><p><strong>mfa_prompt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: <code class="docutils literal notranslate"><span class="pre">&quot;DEVICE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ALWAYS&quot;</span></code>.</p></li>
<li><p><strong>mfa_remember_device</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Remember MFA device. The default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>mfa_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Require MFA. By default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name.</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: <code class="docutils literal notranslate"><span class="pre">&quot;ANYWHERE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ZONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ON_NETWORK&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;OFF_NETWORK&quot;</span></code>.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to exclude. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_includes</span></code>.</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network zones to include. Conflicts with <code class="docutils literal notranslate"><span class="pre">network_excludes</span></code>.</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>session_idle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session can be idle.”,</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session is active: Disable = 0.</p></li>
<li><p><strong>session_persistent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.RuleSignon.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.RuleSignon.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.RuleSignon.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.Signon">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">Signon</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Signon" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Sign On Policy.</p>
<p>This resource allows you to create and configure a Sign On Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.policy.Signon.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Signon.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Signon.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Signon.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Signon.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Signon.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Signon.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Signon.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.policy.Signon.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.policy.Signon.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Signon.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Signon.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Signon resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the policy.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;INACTIVE&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.policy.Signon.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Signon.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.policy.Signon.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.Signon.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_okta.policy.get_default_policy">
<code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">get_default_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.get_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a “Default” policy from Okta. This same thing can be achieved using the <code class="docutils literal notranslate"><span class="pre">policy.getPolicy</span></code> with <code class="docutils literal notranslate"><span class="pre">name</span> <span class="pre">=</span> <span class="pre">&quot;Default&quot;</span></code>, this is simply a shortcut.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>type</strong> (<em>str</em>) – type of policy to retrieve.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_okta.policy.get_policy">
<code class="sig-prename descclassname">pulumi_okta.policy.</code><code class="sig-name descname">get_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.policy.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a policy from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – name of policy to retrieve.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – type of policy to retrieve.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
