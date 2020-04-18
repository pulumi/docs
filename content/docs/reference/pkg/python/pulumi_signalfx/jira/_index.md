---
title: Module jira
title_tag: Module jira | Package pulumi_signalfx | Python SDK
linktitle: jira
notitle: true
---

<div class="section" id="jira">
<h1>jira<a class="headerlink" href="#jira" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.jira"></span><dl class="class">
<dt id="pulumi_signalfx.jira.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.jira.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">assignee_display_name=None</em>, <em class="sig-param">assignee_name=None</em>, <em class="sig-param">auth_method=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issue_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project_key=None</em>, <em class="sig-param">user_email=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.jira.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx Jira integrations. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/admin-guide/integrate-notifications.html#integrate-with-jira">Integration with Jira</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API token for the user email</p></li>
<li><p><strong>assignee_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira display name for the assignee.</p></li>
<li><p><strong>assignee_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira user name for the assignee.</p></li>
<li><p><strong>auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication method used when creating the Jira integration. One of <code class="docutils literal notranslate"><span class="pre">EmailAndToken</span></code> (using <code class="docutils literal notranslate"><span class="pre">user_email</span></code> and <code class="docutils literal notranslate"><span class="pre">api_token</span></code>) or <code class="docutils literal notranslate"><span class="pre">UsernameAndPassword</span></code> (using <code class="docutils literal notranslate"><span class="pre">username</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>).</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base URL of the Jira instance that’s integrated with SignalFx.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>issue_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Issue type (for example, Story) for tickets that Jira creates for detector notifications. SignalFx validates issue types, so you must specify a type that’s valid for the Jira project specified in <code class="docutils literal notranslate"><span class="pre">projectKey</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used to authenticate the Jira integration.</p></li>
<li><p><strong>project_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira key of an existing project. When Jira creates a new ticket for a detector notification, the ticket is assigned to this project.</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address used to authenticate the Jira integration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User name used to authenticate the Jira integration.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.api_token">
<code class="sig-name descname">api_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.api_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The API token for the user email</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.assignee_display_name">
<code class="sig-name descname">assignee_display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.assignee_display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Jira display name for the assignee.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.assignee_name">
<code class="sig-name descname">assignee_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.assignee_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Jira user name for the assignee.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.auth_method">
<code class="sig-name descname">auth_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication method used when creating the Jira integration. One of <code class="docutils literal notranslate"><span class="pre">EmailAndToken</span></code> (using <code class="docutils literal notranslate"><span class="pre">user_email</span></code> and <code class="docutils literal notranslate"><span class="pre">api_token</span></code>) or <code class="docutils literal notranslate"><span class="pre">UsernameAndPassword</span></code> (using <code class="docutils literal notranslate"><span class="pre">username</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.base_url">
<code class="sig-name descname">base_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.base_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Base URL of the Jira instance that’s integrated with SignalFx.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.issue_type">
<code class="sig-name descname">issue_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.issue_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Issue type (for example, Story) for tickets that Jira creates for detector notifications. SignalFx validates issue types, so you must specify a type that’s valid for the Jira project specified in <code class="docutils literal notranslate"><span class="pre">projectKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used to authenticate the Jira integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.project_key">
<code class="sig-name descname">project_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.project_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Jira key of an existing project. When Jira creates a new ticket for a detector notification, the ticket is assigned to this project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.user_email">
<code class="sig-name descname">user_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address used to authenticate the Jira integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.jira.Integration.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.jira.Integration.username" title="Permalink to this definition">¶</a></dt>
<dd><p>User name used to authenticate the Jira integration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.jira.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">assignee_display_name=None</em>, <em class="sig-param">assignee_name=None</em>, <em class="sig-param">auth_method=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issue_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project_key=None</em>, <em class="sig-param">user_email=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.jira.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API token for the user email</p></li>
<li><p><strong>assignee_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira display name for the assignee.</p></li>
<li><p><strong>assignee_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira user name for the assignee.</p></li>
<li><p><strong>auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication method used when creating the Jira integration. One of <code class="docutils literal notranslate"><span class="pre">EmailAndToken</span></code> (using <code class="docutils literal notranslate"><span class="pre">user_email</span></code> and <code class="docutils literal notranslate"><span class="pre">api_token</span></code>) or <code class="docutils literal notranslate"><span class="pre">UsernameAndPassword</span></code> (using <code class="docutils literal notranslate"><span class="pre">username</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>).</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base URL of the Jira instance that’s integrated with SignalFx.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>issue_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Issue type (for example, Story) for tickets that Jira creates for detector notifications. SignalFx validates issue types, so you must specify a type that’s valid for the Jira project specified in <code class="docutils literal notranslate"><span class="pre">projectKey</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used to authenticate the Jira integration.</p></li>
<li><p><strong>project_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Jira key of an existing project. When Jira creates a new ticket for a detector notification, the ticket is assigned to this project.</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address used to authenticate the Jira integration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User name used to authenticate the Jira integration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.jira.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.jira.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.jira.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.jira.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
