---
title: Module pinpoint
title_tag: Module pinpoint | Package pulumi_aws | Python SDK
linktitle: pinpoint
notitle: true
---

<div class="section" id="pinpoint">
<h1>pinpoint<a class="headerlink" href="#pinpoint" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.pinpoint"></span><dl class="class">
<dt id="pulumi_aws.pinpoint.AdmChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">AdmChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.AdmChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.AdmChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AdmChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.AdmChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.AdmChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">ApnsChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.bundle_id">
<code class="sig-name descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.default_authentication_method">
<code class="sig-name descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.token_key">
<code class="sig-name descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsChannel.token_key_id">
<code class="sig-name descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApnsChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">ApnsSandboxChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs Sandbox Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs Sandbox. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.bundle_id">
<code class="sig-name descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.default_authentication_method">
<code class="sig-name descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs Sandbox. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.token_key">
<code class="sig-name descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.token_key_id">
<code class="sig-name descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApnsSandboxChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs Sandbox. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsSandboxChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">ApnsVoipChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs VoIP Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.bundle_id">
<code class="sig-name descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.default_authentication_method">
<code class="sig-name descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.token_key">
<code class="sig-name descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.token_key_id">
<code class="sig-name descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApnsVoipChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">ApnsVoipSandboxChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint APNs VoIP Sandbox Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.bundle_id">
<code class="sig-name descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The pem encoded TLS Certificate from Apple.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.default_authentication_method">
<code class="sig-name descname">default_authentication_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.default_authentication_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key">
<code class="sig-name descname">token_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key_id">
<code class="sig-name descname">token_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.token_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_authentication_method=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">token_key=None</em>, <em class="sig-param">token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApnsVoipSandboxChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pem encoded TLS Certificate from Apple.</p></li>
<li><p><strong>default_authentication_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default authentication method used for APNs. 
<strong>NOTE</strong>: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn’t attempt to use the other authentication type.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Private Key file (ie. <code class="docutils literal notranslate"><span class="pre">.key</span></code> file).</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your Apple developer account team. This value is provided on the Membership page.</p></li>
<li><p><strong>token_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">.p8</span></code> file that you download from your Apple developer account when you create an authentication key.</p></li>
<li><p><strong>token_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.App">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">App</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">campaign_hook=None</em>, <em class="sig-param">limits=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">quiet_time=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint App resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>campaign_hook</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p></li>
<li><p><strong>limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. By default generated by this provider</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Pinpoint application. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code></p></li>
<li><p><strong>quiet_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>campaign_hook</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Lambda function name or ARN to be called for delivery. Conflicts with <code class="docutils literal notranslate"><span class="pre">web_url</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - What mode Lambda should be invoked in. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">DELIVERY</span></code>, <code class="docutils literal notranslate"><span class="pre">FILTER</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with <code class="docutils literal notranslate"><span class="pre">lambda_function_name</span></code></p></li>
</ul>
<p>The <strong>limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">daily</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of messages that the campaign can send daily.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messages_per_second</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">total</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum total number of messages that the campaign can send.</p></li>
</ul>
<p>The <strong>quiet_time</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default end time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">start</span></code> is set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default start time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">end</span></code> is set</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application ID of the Pinpoint App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the PinPoint Application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.campaign_hook">
<code class="sig-name descname">campaign_hook</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.campaign_hook" title="Permalink to this definition">¶</a></dt>
<dd><p>The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Lambda function name or ARN to be called for delivery. Conflicts with <code class="docutils literal notranslate"><span class="pre">web_url</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - What mode Lambda should be invoked in. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">DELIVERY</span></code>, <code class="docutils literal notranslate"><span class="pre">FILTER</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with <code class="docutils literal notranslate"><span class="pre">lambda_function_name</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.limits">
<code class="sig-name descname">limits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.limits" title="Permalink to this definition">¶</a></dt>
<dd><p>The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">daily</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of messages that the campaign can send daily.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messages_per_second</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">total</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum total number of messages that the campaign can send.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The application name. By default generated by this provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Pinpoint application. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.quiet_time">
<code class="sig-name descname">quiet_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.quiet_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default end time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">start</span></code> is set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default start time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">end</span></code> is set</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.App.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.App.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.App.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">campaign_hook=None</em>, <em class="sig-param">limits=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">quiet_time=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing App resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application ID of the Pinpoint App.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the PinPoint Application</p></li>
<li><p><strong>campaign_hook</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p></li>
<li><p><strong>limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. By default generated by this provider</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Pinpoint application. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code></p></li>
<li><p><strong>quiet_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>campaign_hook</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Lambda function name or ARN to be called for delivery. Conflicts with <code class="docutils literal notranslate"><span class="pre">web_url</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - What mode Lambda should be invoked in. Valid values for this parameter are <code class="docutils literal notranslate"><span class="pre">DELIVERY</span></code>, <code class="docutils literal notranslate"><span class="pre">FILTER</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with <code class="docutils literal notranslate"><span class="pre">lambda_function_name</span></code></p></li>
</ul>
<p>The <strong>limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">daily</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of messages that the campaign can send daily.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messages_per_second</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">total</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum total number of messages that the campaign can send.</p></li>
</ul>
<p>The <strong>quiet_time</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default end time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">start</span></code> is set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default start time for quiet time in ISO 8601 format. Required if <code class="docutils literal notranslate"><span class="pre">end</span></code> is set</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.App.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.App.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.BaiduChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">BaiduChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint Baidu Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the Api Key and Secret Key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Baidu.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential Secret key from Baidu.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.api_key">
<code class="sig-name descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential API key from Baidu.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.BaiduChannel.secret_key">
<code class="sig-name descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential Secret key from Baidu.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.BaiduChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">secret_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BaiduChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Baidu.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential Secret key from Baidu.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.BaiduChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.BaiduChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EmailChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">EmailChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">from_address=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint SMS Channel resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address used to send emails from.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an identity verified with SES.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Role used to submit events to Mobile Analytics’ event ingestion service.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.from_address">
<code class="sig-name descname">from_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.from_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address used to send emails from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an identity verified with SES.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.messages_per_second">
<code class="sig-name descname">messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Messages per second that can be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EmailChannel.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM Role used to submit events to Mobile Analytics’ event ingestion service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EmailChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">from_address=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">messages_per_second=None</em>, <em class="sig-param">role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EmailChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address used to send emails from.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an identity verified with SES.</p></li>
<li><p><strong>messages_per_second</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Messages per second that can be sent.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Role used to submit events to Mobile Analytics’ event ingestion service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EmailChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EmailChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EventStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">EventStream</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">destination_stream_arn=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint Event Stream resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>destination_stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.destination_stream_arn">
<code class="sig-name descname">destination_stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.destination_stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.EventStream.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EventStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">destination_stream_arn=None</em>, <em class="sig-param">role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventStream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>destination_stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.EventStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.EventStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.GcmChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">GcmChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint GCM Channel resource.</p>
<blockquote>
<div><p><strong>Note:</strong> Api Key argument will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Google.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.api_key">
<code class="sig-name descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Platform credential API key from Google.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.GcmChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.GcmChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GcmChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Google.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.GcmChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.GcmChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.SmsChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pinpoint.</code><code class="sig-name descname">SmsChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">sender_id=None</em>, <em class="sig-param">short_code=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint SMS Channel resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sender identifier of your messages.</p></li>
<li><p><strong>short_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Short Code registered with the phone provider.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.promotional_messages_per_second">
<code class="sig-name descname">promotional_messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.promotional_messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Promotional messages per second that can be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.sender_id">
<code class="sig-name descname">sender_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.sender_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Sender identifier of your messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.short_code">
<code class="sig-name descname">short_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.short_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The Short Code registered with the phone provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pinpoint.SmsChannel.transactional_messages_per_second">
<code class="sig-name descname">transactional_messages_per_second</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.transactional_messages_per_second" title="Permalink to this definition">¶</a></dt>
<dd><p>Transactional messages per second that can be sent.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.SmsChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">promotional_messages_per_second=None</em>, <em class="sig-param">sender_id=None</em>, <em class="sig-param">short_code=None</em>, <em class="sig-param">transactional_messages_per_second=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SmsChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the channel is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>promotional_messages_per_second</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Promotional messages per second that can be sent.</p></li>
<li><p><strong>sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sender identifier of your messages.</p></li>
<li><p><strong>short_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Short Code registered with the phone provider.</p></li>
<li><p><strong>transactional_messages_per_second</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Transactional messages per second that can be sent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.pinpoint.SmsChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.pinpoint.SmsChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
