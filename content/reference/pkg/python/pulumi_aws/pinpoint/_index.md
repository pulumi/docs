---
---

<div class="section" id="module-pulumi_aws.pinpoint">
<span id="pinpoint"></span><h1>pinpoint<a class="headerlink" href="#module-pulumi_aws.pinpoint" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.pinpoint.AdmChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">AdmChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>client_id=None</em>, <em>client_secret=None</em>, <em>enabled=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</li>
<li><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.client_id">
<code class="descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.client_secret">
<code class="descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.AdmChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.AdmChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</li>
<li><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</li>
<li><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</li>
<li><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</li>
<li><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.bundle_id">
<code class="descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.default_authentication_method">
<code class="descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.team_id">
<code class="descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.token_key">
<code class="descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.token_key_id">
<code class="descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsSandboxChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs Sandbox Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</li>
<li><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs Sandbox. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</li>
<li><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</li>
<li><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</li>
<li><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.bundle_id">
<code class="descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.default_authentication_method">
<code class="descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs Sandbox. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.team_id">
<code class="descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.token_key">
<code class="descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.token_key_id">
<code class="descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsVoipChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs VoIP Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</li>
<li><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</li>
<li><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</li>
<li><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</li>
<li><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.bundle_id">
<code class="descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.default_authentication_method">
<code class="descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.team_id">
<code class="descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.token_key">
<code class="descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.token_key_id">
<code class="descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsVoipSandboxChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs VoIP Sandbox Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</li>
<li><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</li>
<li><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</li>
<li><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</li>
<li><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.bundle_id">
<code class="descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.default_authentication_method">
<code class="descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.team_id">
<code class="descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key">
<code class="descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key_id">
<code class="descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.App">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">App</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>campaign_hook=None</em>, <em>limits=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>quiet_time=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint App resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>campaign_hook</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</li>
<li><strong>limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. By default generated by Terraform</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Pinpoint application. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code></li>
<li><strong>quiet_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application ID of the Pinpoint App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.campaign_hook">
<code class="descname">campaign_hook</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.campaign_hook" title="Permalink to this definition">¶</a></dt>
<dd><p>The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.limits">
<code class="descname">limits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.limits" title="Permalink to this definition">¶</a></dt>
<dd><p>The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The application name. By default generated by Terraform</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Pinpoint application. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.quiet_time">
<code class="descname">quiet_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.quiet_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.App.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.App.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.BaiduChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">BaiduChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_key=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>secret_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint Baidu Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the Api Key and Secret Key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Baidu.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential Secret key from Baidu.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.api_key">
<code class="descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential API key from Baidu.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.secret_key">
<code class="descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential Secret key from Baidu.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.BaiduChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.BaiduChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EmailChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">EmailChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>from_address=None</em>, <em>identity=None</em>, <em>role_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint SMS Channel resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address used to send emails from.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an identity verified with SES.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Role used to submit events to Mobile Analytics’ event ingestion service.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.from_address">
<code class="descname">from_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.from_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address used to send emails from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an identity verified with SES.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.messages_per_second">
<code class="descname">messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Messages per second that can be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM Role used to submit events to Mobile Analytics’ event ingestion service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EmailChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EmailChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EventStream">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">EventStream</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>destination_stream_arn=None</em>, <em>role_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint Event Stream resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>destination_stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.destination_stream_arn">
<code class="descname">destination_stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.destination_stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EventStream.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EventStream.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.GcmChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">GcmChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_key=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint GCM Channel resource.</p>
<blockquote>
<div><strong>Note:</strong> Api Key argument will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Google.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.api_key">
<code class="descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential API key from Google.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.GcmChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.GcmChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.SmsChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">SmsChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>sender_id=None</em>, <em>short_code=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint SMS Channel resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sender identifier of your messages.</li>
<li><strong>short_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Short Code registered with the phone provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.promotional_messages_per_second">
<code class="descname">promotional_messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.promotional_messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Promotional messages per second that can be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.sender_id">
<code class="descname">sender_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.sender_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Sender identifier of your messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.short_code">
<code class="descname">short_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.short_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The Short Code registered with the phone provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.transactional_messages_per_second">
<code class="descname">transactional_messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.transactional_messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Transactional messages per second that can be sent.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.SmsChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.SmsChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
