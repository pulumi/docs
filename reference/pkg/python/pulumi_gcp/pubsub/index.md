<div class="section" id="module-pulumi_gcp.pubsub">
<span id="pubsub"></span><h1>pubsub<a class="headerlink" href="#module-pulumi_gcp.pubsub" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.pubsub.Subscription">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">Subscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ack_deadline_seconds=None</em>, <em>name=None</em>, <em>project=None</em>, <em>push_config=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a subscription in Google’s pubsub queueing system. For more information see
<a class="reference external" href="https://cloud.google.com/pubsub/docs">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ack_deadline_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of seconds a
subscriber has to acknowledge a received message, otherwise the message is
redelivered. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by pubsub.
Changing this forces a new resource to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>push_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Block configuration for push options. More
configuration options are detailed below.</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic name or id to bind this subscription to, required by pubsub.
Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.ack_deadline_seconds">
<code class="descname">ack_deadline_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.ack_deadline_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of seconds a
subscriber has to acknowledge a received message, otherwise the message is
redelivered. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by pubsub.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path of the subscription in the format <code class="docutils literal notranslate"><span class="pre">projects/{project}/subscriptions/{sub}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.push_config">
<code class="descname">push_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.push_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Block configuration for push options. More
configuration options are detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Subscription.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The topic name or id to bind this subscription to, required by pubsub.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.Subscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.Subscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">SubscriptionIAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em>, <em>subscription=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] project: The project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>subscription</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subscription’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.subscription">
<code class="descname">subscription</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">SubscriptionIAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em>, <em>subscription=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] project: The project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>subscription</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subscription’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.subscription">
<code class="descname">subscription</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">SubscriptionIAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_data=None</em>, <em>project=None</em>, <em>subscription=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_subscription_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>subscription</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subscription’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.subscription">
<code class="descname">subscription</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.SubscriptionIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.SubscriptionIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.Topic">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">Topic</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a topic in Google’s pubsub queueing system. For more information see
<a class="reference external" href="https://cloud.google.com/pubsub/docs">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the pubsub topic.
Changing this forces a new resource to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Topic.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the pubsub topic.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.Topic.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.Topic.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.Topic.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.Topic.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">TopicIAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code>: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] project: The project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the topic’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The topic name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">TopicIAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code>: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] project: The project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the topic’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMMember.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The topic name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.TopicIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.pubsub.</code><code class="descname">TopicIAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_data=None</em>, <em>project=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code>: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_pubsub_topic_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic name or id to bind to attach IAM policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the topic’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The topic name or id to bind to attach IAM policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.pubsub.TopicIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.pubsub.TopicIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
