---
---

<div class="section" id="organizations">
<h1>organizations<a class="headerlink" href="#organizations" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.organizations"></span><dl class="class">
<dt id="pulumi_aws.organizations.Account">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>email=None</em>, <em>iam_user_access_to_billing=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>role_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Account resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</li>
<li><strong>iam_user_access_to_billing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <code class="docutils literal notranslate"><span class="pre">DENY</span></code>, then only the root user of the new account can access account billing information.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the member account.</li>
<li><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID. A configuration must be present for this argument to perform drift detection.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_account.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_account.html.markdown</a>.</div></blockquote>
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
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <code class="docutils literal notranslate"><span class="pre">DENY</span></code>, then only the root user of the new account can access account billing information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the member account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID. A configuration must be present for this argument to perform drift detection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Organization</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aws_service_access_principals=None</em>, <em>enabled_policy_types=None</em>, <em>feature_set=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an organization.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aws_service_access_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</li>
<li><strong>enabled_policy_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Organizations policy types to enable in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</li>
<li><strong>feature_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organization.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organization.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.accounts">
<code class="descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts including the master account. For a list excluding the master account, see the <code class="docutils literal notranslate"><span class="pre">non_master_accounts</span></code> attribute. All elements have these attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the root</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.aws_service_access_principals">
<code class="descname">aws_service_access_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.aws_service_access_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.enabled_policy_types">
<code class="descname">enabled_policy_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.enabled_policy_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Organizations policy types to enable in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</p>
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

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.non_master_accounts">
<code class="descname">non_master_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.non_master_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts excluding the master account. For a list including the master account, see the <code class="docutils literal notranslate"><span class="pre">accounts</span></code> attribute. All elements have these attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.roots">
<code class="descname">roots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.roots" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization roots. All elements have these attributes:</p>
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
<dt id="pulumi_aws.organizations.OrganizationalUnit">
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">OrganizationalUnit</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an organizational unit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the organizational unit</li>
<li><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the parent organizational unit, which may be the root</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organizational_unit.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organizational_unit.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.accounts">
<code class="descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of child accounts for this Organizational Unit. Does not return account information for child Organizational Units. All elements have these attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the organizational unit</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the organizational unit</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the parent organizational unit, which may be the root</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.OrganizationalUnit.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.OrganizationalUnit.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>content=None</em>, <em>description=None</em>, <em>name=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage an <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html">AWS Organizations policy</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy content to add to the new policy. For example, if you create a <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">service control policy (SCP)</a>, this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">Service Control Policy Syntax documentation</a>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to assign to the policy.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to assign to the policy.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of policy to create. Currently, the only valid value is <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> (SCP).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy content to add to the new policy. For example, if you create a <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">service control policy (SCP)</a>, this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">Service Control Policy Syntax documentation</a>.</p>
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
<dd><p>The type of policy to create. Currently, the only valid value is <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> (SCP).</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.organizations.</code><code class="descname">PolicyAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_id=None</em>, <em>target_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the policy that you want to attach to the target.</li>
<li><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_policy_attachment.html.markdown</a>.</div></blockquote>
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
