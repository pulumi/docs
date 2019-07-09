---
---

<div class="section" id="module-pulumi_aws.glacier">
<span id="glacier"></span><h1>glacier<a class="headerlink" href="#module-pulumi_aws.glacier" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.glacier.Vault">
<em class="property">class </em><code class="descclassname">pulumi_aws.glacier.</code><code class="descname">Vault</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_policy=None</em>, <em>name=None</em>, <em>notifications=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glacier Vault Resource. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html">Glacier Developer Guide</a> for a full explanation of the Glacier Vault functionality</p>
<blockquote>
<div><strong>NOTE:</strong> When removing a Glacier Vault, the Vault must be empty.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access*policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy document. This is a JSON formatted string.
The heredoc syntax or <code class="docutils literal notranslate"><span class="pre">file</span></code> function is helpful here. Use the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">Glacier Developer Guide</a> for more information on Glacier Vault Policy</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘<a href="#id4"><span class="problematic" id="id5">*</span></a>’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</li>
<li><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notifications for the Vault. Fields documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glacier_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glacier_vault.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.access_policy">
<code class="descname">access_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.
The heredoc syntax or <code class="docutils literal notranslate"><span class="pre">file</span></code> function is helpful here. Use the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">Glacier Developer Guide</a> for more information on Glacier Vault Policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the vault that was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘_’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.notifications">
<code class="descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The notifications for the Vault. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.Vault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.Vault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.VaultLock">
<em class="property">class </em><code class="descclassname">pulumi_aws.glacier.</code><code class="descname">VaultLock</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>complete_lock=None</em>, <em>ignore_deletion_error=None</em>, <em>policy=None</em>, <em>vault_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VaultLock resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</li>
<li><strong>vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glacier Vault.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glacier_vault_lock.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glacier_vault_lock.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.vault_name">
<code class="descname">vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Glacier Vault.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.VaultLock.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.VaultLock.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
