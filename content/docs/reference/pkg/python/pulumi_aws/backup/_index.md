---
---

<div class="section" id="module-pulumi_aws.backup">
<span id="backup"></span><h1>backup<a class="headerlink" href="#module-pulumi_aws.backup" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.backup.Plan">
<em class="property">class </em><code class="descclassname">pulumi_aws.backup.</code><code class="descname">Plan</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>rules=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Backup plan resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of a backup plan.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule object that specifies a scheduled task that is used to back up a selection of resources.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata that you can assign to help organize the plans you create.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.backup.Plan.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Plan.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the backup plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Plan.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Plan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of a backup plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Plan.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Plan.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule object that specifies a scheduled task that is used to back up a selection of resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Plan.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Plan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata that you can assign to help organize the plans you create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Plan.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Plan.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backup plan.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.backup.Plan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Plan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.backup.Plan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Plan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.backup.Selection">
<em class="property">class </em><code class="descclassname">pulumi_aws.backup.</code><code class="descname">Selection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>iam_role_arn=None</em>, <em>name=None</em>, <em>plan_id=None</em>, <em>resources=None</em>, <em>selection_tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Selection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages selection conditions for AWS Backup plan resources.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the <a class="reference external" href="https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies">AWS Backup Developer Guide</a> for additional information about using AWS managed policies or creating custom policies attached to the IAM role.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of a resource selection document.</li>
<li><strong>plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The backup plan ID to be associated with the selection of resources.</li>
<li><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..</li>
<li><strong>selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tag-based conditions used to specify a set of resources to assign to a backup plan.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.backup.Selection.iam_role_arn">
<code class="descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Selection.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the <a class="reference external" href="https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies">AWS Backup Developer Guide</a> for additional information about using AWS managed policies or creating custom policies attached to the IAM role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Selection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Selection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of a resource selection document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Selection.plan_id">
<code class="descname">plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Selection.plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The backup plan ID to be associated with the selection of resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Selection.resources">
<code class="descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Selection.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Selection.selection_tags">
<code class="descname">selection_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Selection.selection_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag-based conditions used to specify a set of resources to assign to a backup plan.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.backup.Selection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Selection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.backup.Selection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Selection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.backup.Vault">
<em class="property">class </em><code class="descclassname">pulumi_aws.backup.</code><code class="descname">Vault</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>kms_key_arn=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Backup vault resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The server-side encryption key that is used to protect your backups.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the backup vault to create.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata that you can assign to help organize the resources that you create.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.backup.Vault.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Vault.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Vault.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Vault.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-side encryption key that is used to protect your backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Vault.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the backup vault to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Vault.recovery_points">
<code class="descname">recovery_points</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Vault.recovery_points" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of recovery points that are stored in a backup vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.backup.Vault.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.backup.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata that you can assign to help organize the resources that you create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.backup.Vault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.backup.Vault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.backup.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
