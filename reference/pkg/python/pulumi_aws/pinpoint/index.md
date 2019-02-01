<div class="section" id="module-pulumi_aws.pinpoint">
<span id="pinpoint"></span><h1>pinpoint<a class="headerlink" href="#module-pulumi_aws.pinpoint" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.pinpoint.AdmChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">AdmChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>client_id=None</em>, <em>client_secret=None</em>, <em>enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.AdmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.</p>
<p>&gt; <strong>Note:</strong> All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.</li>
<li><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <cite>true</cite>.</li>
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
<dd><p>Specifies whether to enable the channel. Defaults to <cite>true</cite>.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ApnsChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[str] bundle_id
:param pulumi.Input[str] certificate
:param pulumi.Input[str] default_authentication_method
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] private_key
:param pulumi.Input[str] team_id
:param pulumi.Input[str] token_key
:param pulumi.Input[str] token_key_id</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsSandboxChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ApnsSandboxChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[str] bundle_id
:param pulumi.Input[str] certificate
:param pulumi.Input[str] default_authentication_method
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] private_key
:param pulumi.Input[str] team_id
:param pulumi.Input[str] token_key
:param pulumi.Input[str] token_key_id</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsVoipChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ApnsVoipChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[str] bundle_id
:param pulumi.Input[str] certificate
:param pulumi.Input[str] default_authentication_method
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] private_key
:param pulumi.Input[str] team_id
:param pulumi.Input[str] token_key
:param pulumi.Input[str] token_key_id</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">ApnsVoipSandboxChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>bundle_id=None</em>, <em>certificate=None</em>, <em>default_authentication_method=None</em>, <em>enabled=None</em>, <em>private_key=None</em>, <em>team_id=None</em>, <em>token_key=None</em>, <em>token_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.ApnsVoipSandboxChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ApnsVoipSandboxChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[str] bundle_id
:param pulumi.Input[str] certificate
:param pulumi.Input[str] default_authentication_method
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] private_key
:param pulumi.Input[str] team_id
:param pulumi.Input[str] token_key
:param pulumi.Input[str] token_key_id</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">App</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>campaign_hook=None</em>, <em>limits=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>quiet_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.App" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint App resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>campaign_hook</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</li>
<li><strong>limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. By default generated by Terraform</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Pinpoint application. Conflicts with <cite>name</cite></li>
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
<dd><p>The name of the Pinpoint application. Conflicts with <cite>name</cite></p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">BaiduChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_key=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>secret_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.BaiduChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Pinpoint Baidu Channel resource.</p>
<p>&gt; <strong>Note:</strong> All arguments including the Api Key and Secret Key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platform credential API key from Baidu.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application ID.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable the channel. Defaults to <cite>true</cite>.</li>
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
<dd><p>Specifies whether to enable the channel. Defaults to <cite>true</cite>.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">EmailChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>from_address=None</em>, <em>identity=None</em>, <em>role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EmailChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EmailChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] from_address
:param pulumi.Input[str] identity
:param pulumi.Input[str] role_arn</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">EventStream</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>destination_stream_arn=None</em>, <em>role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.EventStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EventStream resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[str] destination_stream_arn
:param pulumi.Input[str] role_arn</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">GcmChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_key=None</em>, <em>application_id=None</em>, <em>enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.GcmChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GcmChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] api_key
:param pulumi.Input[str] application_id
:param pulumi.Input[bool] enabled</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.pinpoint.</code><code class="descname">SmsChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>enabled=None</em>, <em>sender_id=None</em>, <em>short_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pinpoint.SmsChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SmsChannel resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] application_id
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] sender_id
:param pulumi.Input[str] short_code</p>
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
