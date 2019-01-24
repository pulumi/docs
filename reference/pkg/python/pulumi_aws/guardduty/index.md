<div class="section" id="module-pulumi_aws.guardduty">
<span id="guardduty"></span><h1>guardduty<a class="headerlink" href="#module-pulumi_aws.guardduty" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.guardduty.Detector">
<em class="property">class </em><code class="descclassname">pulumi_aws.guardduty.</code><code class="descname">Detector</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>enable=None</em>, <em>finding_publishing_frequency=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty detector.</p>
<p>&gt; <strong>NOTE:</strong> Deleting this resource is equivalent to “disabling” GuardDuty for an AWS region, which removes all existing findings. You can set the <cite>enable</cite> attribute to <cite>false</cite> to instead “suspend” monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html">https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html</a>) for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable monitoring and feedback reporting. Setting to <cite>false</cite> is equivalent to “suspending” GuardDuty. Defaults to <cite>true</cite>.</li>
<li><strong>finding_publishing_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the frequency of notifications sent for subsequent finding occurrences. Valid values: <cite>FIFTEEN_MINUTES, ONE_HOUR, SIX_HOURS</cite>. Default: <cite>SIX_HOURS</cite>. See [AWS Documentation](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency">https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency</a>) for more information.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.guardduty.Detector.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the GuardDuty detector</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Detector.enable">
<code class="descname">enable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable monitoring and feedback reporting. Setting to <cite>false</cite> is equivalent to “suspending” GuardDuty. Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Detector.finding_publishing_frequency">
<code class="descname">finding_publishing_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Detector.finding_publishing_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the frequency of notifications sent for subsequent finding occurrences. Valid values: <cite>FIFTEEN_MINUTES, ONE_HOUR, SIX_HOURS</cite>. Default: <cite>SIX_HOURS</cite>. See [AWS Documentation](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency">https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency</a>) for more information.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.Detector.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.Detector.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Detector.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.guardduty.IPSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.guardduty.</code><code class="descname">IPSet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>activate=None</em>, <em>detector_id=None</em>, <em>format=None</em>, <em>location=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty IPSet.</p>
<p>&gt; <strong>Note:</strong> Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html">https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html</a>)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded IPSet.</li>
<li><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</li>
<li><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the IPSet. Valid values: <cite>TXT</cite> | <cite>STIX</cite> | <cite>OTX_CSV</cite> | <cite>ALIEN_VAULT</cite> | <cite>PROOF_POINT</cite> | <cite>FIRE_EYE</cite></li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the IPSet.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the IPSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.guardduty.IPSet.activate">
<code class="descname">activate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether GuardDuty is to start using the uploaded IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.IPSet.detector_id">
<code class="descname">detector_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.IPSet.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the file that contains the IPSet. Valid values: <cite>TXT</cite> | <cite>STIX</cite> | <cite>OTX_CSV</cite> | <cite>ALIEN_VAULT</cite> | <cite>PROOF_POINT</cite> | <cite>FIRE_EYE</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.IPSet.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the file that contains the IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.IPSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to identify the IPSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.IPSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.IPSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.IPSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.guardduty.Member">
<em class="property">class </em><code class="descclassname">pulumi_aws.guardduty.</code><code class="descname">Member</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>account_id=None</em>, <em>detector_id=None</em>, <em>disable_email_notification=None</em>, <em>email=None</em>, <em>invitation_message=None</em>, <em>invite=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty member.</p>
<p>&gt; <strong>NOTE:</strong> Currently after using this resource, you must manually accept member account invitations before GuardDuty will begin sending cross-account events. More information for how to accomplish this via the AWS Console or API can be found in the [GuardDuty User Guide](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html">https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html</a>). Terraform implementation of the member acceptance resource can be tracked in [Github](<a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues/2489">https://github.com/terraform-providers/terraform-provider-aws/issues/2489</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID for member account.</li>
<li><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty account where you want to create member accounts.</li>
<li><strong>disable_email_notification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether an email notification is sent to the accounts. Defaults to <cite>false</cite>.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for member account.</li>
<li><strong>invitation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message for invitation.</li>
<li><strong>invite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to invite the account to GuardDuty as a member. Defaults to <cite>false</cite>. To detect if an invitation needs to be (re-)sent, the Terraform state value is <cite>true</cite> based on a <cite>relationship_status</cite> of <cite>Disabled</cite>, <cite>Enabled</cite>, <cite>Invited</cite>, or <cite>EmailVerificationInProgress</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID for member account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.detector_id">
<code class="descname">detector_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty account where you want to create member accounts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.disable_email_notification">
<code class="descname">disable_email_notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.disable_email_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether an email notification is sent to the accounts. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for member account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.invitation_message">
<code class="descname">invitation_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.invitation_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Message for invitation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.invite">
<code class="descname">invite</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.invite" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to invite the account to GuardDuty as a member. Defaults to <cite>false</cite>. To detect if an invitation needs to be (re-)sent, the Terraform state value is <cite>true</cite> based on a <cite>relationship_status</cite> of <cite>Disabled</cite>, <cite>Enabled</cite>, <cite>Invited</cite>, or <cite>EmailVerificationInProgress</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.Member.relationship_status">
<code class="descname">relationship_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.Member.relationship_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html">https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html</a>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.Member.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.Member.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.Member.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.guardduty.ThreatIntelSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.guardduty.</code><code class="descname">ThreatIntelSet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>activate=None</em>, <em>detector_id=None</em>, <em>format=None</em>, <em>location=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a GuardDuty ThreatIntelSet.</p>
<p>&gt; <strong>Note:</strong> Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](<a class="reference external" href="https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html">https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html</a>)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.</li>
<li><strong>detector_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detector ID of the GuardDuty.</li>
<li><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the file that contains the ThreatIntelSet. Valid values: <cite>TXT</cite> | <cite>STIX</cite> | <cite>OTX_CSV</cite> | <cite>ALIEN_VAULT</cite> | <cite>PROOF_POINT</cite> | <cite>FIRE_EYE</cite></li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the file that contains the ThreatIntelSet.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to identify the ThreatIntelSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.activate">
<code class="descname">activate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.detector_id">
<code class="descname">detector_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.detector_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The detector ID of the GuardDuty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the file that contains the ThreatIntelSet. Valid values: <cite>TXT</cite> | <cite>STIX</cite> | <cite>OTX_CSV</cite> | <cite>ALIEN_VAULT</cite> | <cite>PROOF_POINT</cite> | <cite>FIRE_EYE</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the file that contains the ThreatIntelSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to identify the ThreatIntelSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.guardduty.ThreatIntelSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.guardduty.ThreatIntelSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
