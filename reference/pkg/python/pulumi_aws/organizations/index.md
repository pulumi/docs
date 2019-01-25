<div class="section" id="module-pulumi_aws.organizations">
<span id="organizations"></span><h1>organizations<a class="headerlink" href="#module-pulumi_aws.organizations" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.organizations.Account">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>email=None</em>, <em>iam_user_access_to_billing=None</em>, <em>name=None</em>, <em>role_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a member account in the current organization.</p>
<p>&gt; <strong>Note:</strong> Account management must be done from the organization’s master account.</p>
<p>!&gt; <strong>WARNING:</strong> Deleting this Terraform resource will only remove an AWS account from an organization. Terraform will not close the account. The member account must be prepared to be a standalone account beforehand. See the [AWS Organizations documentation](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html</a>) for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</li>
<li><strong>iam_user_access_to_billing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <cite>ALLOW</cite>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <cite>DENY</cite>, then only the root user of the new account can access account billing information.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the member account.</li>
<li><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for this account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.iam_user_access_to_billing">
<code class="descname">iam_user_access_to_billing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.iam_user_access_to_billing" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <cite>ALLOW</cite>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <cite>DENY</cite>, then only the root user of the new account can access account billing information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the member account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.role_name">
<code class="descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Organization">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Organization</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>aws_service_access_principals=None</em>, <em>feature_set=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an organization.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aws_service_access_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <cite>feature_set</cite> set to <cite>ALL</cite>. For additional information, see the [AWS Organizations User Guide](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html</a>).</li>
<li><strong>feature_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the organization</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.aws_service_access_principals">
<code class="descname">aws_service_access_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.aws_service_access_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <cite>feature_set</cite> set to <cite>ALL</cite>. For additional information, see the [AWS Organizations User Guide](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.feature_set">
<code class="descname">feature_set</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.feature_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_arn">
<code class="descname">master_account_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the master account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_email">
<code class="descname">master_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the master account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_id">
<code class="descname">master_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the master account</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Organization.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Organization.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Policy">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content=None</em>, <em>description=None</em>, <em>name=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage an [AWS Organizations policy](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html</a>), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html</a>).</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to assign to the policy.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to assign to the policy.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of policy to create. Currently, the only valid value is <cite>SERVICE_CONTROL_POLICY</cite> (SCP).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html</a>), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](<a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description to assign to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to assign to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of policy to create. Currently, the only valid value is <cite>SERVICE_CONTROL_POLICY</cite> (SCP).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.PolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">PolicyAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>policy_id=None</em>, <em>target_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the policy that you want to attach to the target.</li>
<li><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.organizations.PolicyAttachment.policy_id">
<code class="descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier (ID) of the policy that you want to attach to the target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.PolicyAttachment.target_id">
<code class="descname">target_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.PolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.PolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
