---
title: Module organizations
title_tag: Module organizations | Package pulumi_aws | Python SDK
linktitle: organizations
notitle: true
---

<div class="section" id="organizations">
<h1>organizations<a class="headerlink" href="#organizations" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.organizations"></span><dl class="class">
<dt id="pulumi_aws.organizations.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">iam_user_access_to_billing=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a member account in the current organization.</p>
<blockquote>
<div><p><strong>Note:</strong> Account management must be done from the organization’s master account.</p>
</div></blockquote>
<p>!&gt; <strong>WARNING:</strong> Deleting this resource will only remove an AWS account from an organization. This provider will not close the account. The member account must be prepared to be a standalone account beforehand. See the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html">AWS Organizations documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</p></li>
<li><p><strong>iam_user_access_to_billing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <code class="docutils literal notranslate"><span class="pre">DENY</span></code>, then only the root user of the new account can access account billing information.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the member account.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID. A configuration must be present for this argument to perform drift detection.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account. The Organizations API provides no method for reading this information after account creation, so this provider cannot perform drift detection on its value and will always show a difference for a configured value after import unless <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ is used.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for this account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.iam_user_access_to_billing">
<code class="sig-name descname">iam_user_access_to_billing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.iam_user_access_to_billing" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <code class="docutils literal notranslate"><span class="pre">DENY</span></code>, then only the root user of the new account can access account billing information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the member account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID. A configuration must be present for this argument to perform drift detection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account. The Organizations API provides no method for reading this information after account creation, so this provider cannot perform drift detection on its value and will always show a difference for a configured value after import unless <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">iam_user_access_to_billing=None</em>, <em class="sig-param">joined_method=None</em>, <em class="sig-param">joined_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for this account.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.</p></li>
<li><p><strong>iam_user_access_to_billing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, the new account enables IAM users to access account billing information if they have the required permissions. If set to <code class="docutils literal notranslate"><span class="pre">DENY</span></code>, then only the root user of the new account can access account billing information.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the member account.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID. A configuration must be present for this argument to perform drift detection.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account. The Organizations API provides no method for reading this information after account creation, so this provider cannot perform drift detection on its value and will always show a difference for a configured value after import unless <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ is used.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.AwaitableGetOrganizationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">AwaitableGetOrganizationResult</code><span class="sig-paren">(</span><em class="sig-param">accounts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_service_access_principals=None</em>, <em class="sig-param">enabled_policy_types=None</em>, <em class="sig-param">feature_set=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_account_arn=None</em>, <em class="sig-param">master_account_email=None</em>, <em class="sig-param">master_account_id=None</em>, <em class="sig-param">non_master_accounts=None</em>, <em class="sig-param">roots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.AwaitableGetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.organizations.AwaitableGetOrganizationalUnitsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">AwaitableGetOrganizationalUnitsResult</code><span class="sig-paren">(</span><em class="sig-param">childrens=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">parent_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.AwaitableGetOrganizationalUnitsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.organizations.GetOrganizationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">GetOrganizationResult</code><span class="sig-paren">(</span><em class="sig-param">accounts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_service_access_principals=None</em>, <em class="sig-param">enabled_policy_types=None</em>, <em class="sig-param">feature_set=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_account_arn=None</em>, <em class="sig-param">master_account_email=None</em>, <em class="sig-param">master_account_id=None</em>, <em class="sig-param">non_master_accounts=None</em>, <em class="sig-param">roots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganization.</p>
<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.accounts">
<code class="sig-name descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts including the master account. For a list excluding the master account, see the <code class="docutils literal notranslate"><span class="pre">non_master_accounts</span></code> attribute. All elements have these attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the root</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.aws_service_access_principals">
<code class="sig-name descname">aws_service_access_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.aws_service_access_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AWS service principal names that have integration enabled with your organization. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.enabled_policy_types">
<code class="sig-name descname">enabled_policy_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.enabled_policy_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Organizations policy types that are enabled in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.feature_set">
<code class="sig-name descname">feature_set</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.feature_set" title="Permalink to this definition">¶</a></dt>
<dd><p>The FeatureSet of the organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.master_account_arn">
<code class="sig-name descname">master_account_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.master_account_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.master_account_email">
<code class="sig-name descname">master_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.master_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address that is associated with the AWS account that is designated as the master account for the organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.master_account_id">
<code class="sig-name descname">master_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier (ID) of the master account of an organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.non_master_accounts">
<code class="sig-name descname">non_master_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.non_master_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts excluding the master account. For a list including the master account, see the <code class="docutils literal notranslate"><span class="pre">accounts</span></code> attribute. All elements have these attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationResult.roots">
<code class="sig-name descname">roots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationResult.roots" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization roots. All elements have these attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.organizations.GetOrganizationalUnitsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">GetOrganizationalUnitsResult</code><span class="sig-paren">(</span><em class="sig-param">childrens=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">parent_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationalUnitsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganizationalUnits.</p>
<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationalUnitsResult.childrens">
<code class="sig-name descname">childrens</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationalUnitsResult.childrens" title="Permalink to this definition">¶</a></dt>
<dd><p>List of child organizational units, which have the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.GetOrganizationalUnitsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.GetOrganizationalUnitsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.organizations.Organization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">Organization</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_service_access_principals=None</em>, <em class="sig-param">enabled_policy_types=None</em>, <em class="sig-param">feature_set=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an organization.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_service_access_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</p>
</p></li>
<li><p><strong>enabled_policy_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of Organizations policy types to enable in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</p>
</p></li>
<li><p><strong>feature_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.accounts">
<code class="sig-name descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts including the master account. For a list excluding the master account, see the <code class="docutils literal notranslate"><span class="pre">non_master_accounts</span></code> attribute. All elements have these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the policy type as it relates to the associated root</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the root</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.aws_service_access_principals">
<code class="sig-name descname">aws_service_access_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.aws_service_access_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.enabled_policy_types">
<code class="sig-name descname">enabled_policy_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.enabled_policy_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Organizations policy types to enable in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.feature_set">
<code class="sig-name descname">feature_set</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.feature_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_arn">
<code class="sig-name descname">master_account_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the master account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_email">
<code class="sig-name descname">master_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the master account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.master_account_id">
<code class="sig-name descname">master_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the master account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.non_master_accounts">
<code class="sig-name descname">non_master_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.non_master_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization accounts excluding the master account. For a list including the master account, see the <code class="docutils literal notranslate"><span class="pre">accounts</span></code> attribute. All elements have these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the policy type as it relates to the associated root</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Organization.roots">
<code class="sig-name descname">roots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Organization.roots" title="Permalink to this definition">¶</a></dt>
<dd><p>List of organization roots. All elements have these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of policy types enabled for this root. All elements have these attributes:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the policy type as it relates to the associated root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Organization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accounts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_service_access_principals=None</em>, <em class="sig-param">enabled_policy_types=None</em>, <em class="sig-param">feature_set=None</em>, <em class="sig-param">master_account_arn=None</em>, <em class="sig-param">master_account_email=None</em>, <em class="sig-param">master_account_id=None</em>, <em class="sig-param">non_master_accounts=None</em>, <em class="sig-param">roots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Organization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of organization accounts including the master account. For a list excluding the master account, see the <code class="docutils literal notranslate"><span class="pre">non_master_accounts</span></code> attribute. All elements have these attributes:</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the root</p></li>
<li><p><strong>aws_service_access_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">AWS Organizations User Guide</a>.</p>
</p></li>
<li><p><strong>enabled_policy_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of Organizations policy types to enable in the Organization Root. Organization must have <code class="docutils literal notranslate"><span class="pre">feature_set</span></code> set to <code class="docutils literal notranslate"><span class="pre">ALL</span></code>. For additional information about valid policy types (e.g. <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>), see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html">AWS Organizations API Reference</a>.</p>
</p></li>
<li><p><strong>feature_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify “ALL” (default) or “CONSOLIDATED_BILLING”.</p></li>
<li><p><strong>master_account_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the master account</p></li>
<li><p><strong>master_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the master account</p></li>
<li><p><strong>master_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the master account</p></li>
<li><p><strong>non_master_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of organization accounts excluding the master account. For a list including the master account, see the <code class="docutils literal notranslate"><span class="pre">accounts</span></code> attribute. All elements have these attributes:</p></li>
<li><p><strong>roots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of organization roots. All elements have these attributes:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the policy type as it relates to the associated root</p></li>
</ul>
<p>The <strong>non_master_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the policy type as it relates to the associated root</p></li>
</ul>
<p>The <strong>roots</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the policy type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of policy types enabled for this root. All elements have these attributes:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the policy type as it relates to the associated root</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Organization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Organization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Organization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.OrganizationalUnit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">OrganizationalUnit</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an organizational unit.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the organizational unit</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the parent organizational unit, which may be the root</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.accounts">
<code class="sig-name descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of child accounts for this Organizational Unit. Does not return account information for child Organizational Units. All elements have these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the organizational unit</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the organization unit</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name for the organizational unit</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the organizational unit</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the organizational unit</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.OrganizationalUnit.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the parent organizational unit, which may be the root</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.OrganizationalUnit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accounts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationalUnit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of child accounts for this Organizational Unit. Does not return account information for child Organizational Units. All elements have these attributes:</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the organizational unit</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the organizational unit</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the parent organizational unit, which may be the root</p></li>
</ul>
</dd>
</dl>
<p>The <strong>accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the organizational unit</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email of the account</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the organization unit</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the organizational unit</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.OrganizationalUnit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.OrganizationalUnit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.OrganizationalUnit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage an <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html">AWS Organizations policy</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy content to add to the new policy. For example, if you create a <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">service control policy (SCP)</a>, this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">Service Control Policy Syntax documentation</a> and for more information on the Tag Policy syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html">Tag Policy Syntax documentation</a>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to assign to the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to assign to the policy.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of policy to create. Currently, the only valid values are <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> (SCP) and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy content to add to the new policy. For example, if you create a <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">service control policy (SCP)</a>, this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">Service Control Policy Syntax documentation</a> and for more information on the Tag Policy syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html">Tag Policy Syntax documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description to assign to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name to assign to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.Policy.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.Policy.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of policy to create. Currently, the only valid values are <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> (SCP) and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the policy.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy content to add to the new policy. For example, if you create a <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">service control policy (SCP)</a>, this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html">Service Control Policy Syntax documentation</a> and for more information on the Tag Policy syntax, see the <a class="reference external" href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html">Tag Policy Syntax documentation</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to assign to the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name to assign to the policy.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of policy to create. Currently, the only valid values are <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code> (SCP) and <code class="docutils literal notranslate"><span class="pre">TAG_POLICY</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SERVICE_CONTROL_POLICY</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.PolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">PolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">target_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the policy that you want to attach to the target.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.organizations.PolicyAttachment.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier (ID) of the policy that you want to attach to the target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.organizations.PolicyAttachment.target_id">
<code class="sig-name descname">target_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.PolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">target_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the policy that you want to attach to the target.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.organizations.PolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.organizations.PolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.organizations.get_organization">
<code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">get_organization</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.get_organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about the organization that the user’s account belongs to</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.organizations.get_organizational_units">
<code class="sig-prename descclassname">pulumi_aws.organizations.</code><code class="sig-name descname">get_organizational_units</code><span class="sig-paren">(</span><em class="sig-param">parent_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.organizations.get_organizational_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Get all direct child organizational units under a parent organizational unit. This only provides immediate children, not all children.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>parent_id</strong> (<em>str</em>) – The parent ID of the organizational unit.</p>
</dd>
</dl>
</dd></dl>

</div>
