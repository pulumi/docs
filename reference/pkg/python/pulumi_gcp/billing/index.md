<div class="section" id="module-pulumi_gcp.billing">
<span id="billing"></span><h1>billing<a class="headerlink" href="#module-pulumi_gcp.billing" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.billing.AccountIamBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.billing.</code><code class="descname">AccountIamBinding</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_account_id=None</em>, <em>members=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Billing Account.</p>
<dl class="docutils">
<dt>&gt; <strong>Note:</strong> This resource __must <a href="#id1"><span class="problematic" id="id2">not__</span></a> be used in conjunction with</dt>
<dd><cite>google_billing_account_iam_member</cite> for the __same <a href="#id1"><span class="problematic" id="id3">role__</span></a> or they will fight over
what your policy should be.</dd>
</dl>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</li>
<li><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that the role should apply to.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.billing_account_id">
<code class="descname">billing_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the billing account’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.members">
<code class="descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that the role should apply to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.billing.AccountIamMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.billing.</code><code class="descname">AccountIamMember</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_account_id=None</em>, <em>member=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Billing Account.</p>
<dl class="docutils">
<dt>&gt; <strong>Note:</strong> This resource __must <a href="#id1"><span class="problematic" id="id4">not__</span></a> be used in conjunction with</dt>
<dd><cite>google_billing_account_iam_binding</cite> for the __same <a href="#id1"><span class="problematic" id="id5">role__</span></a> or they will fight over
what your policy should be.</dd>
</dl>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</li>
<li><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user that the role should apply to.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.billing_account_id">
<code class="descname">billing_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the billing account’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.member">
<code class="descname">member</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.member" title="Permalink to this definition">¶</a></dt>
<dd><p>The user that the role should apply to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.billing.AccountIamPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.billing.</code><code class="descname">AccountIamPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_account_id=None</em>, <em>policy_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of the entire IAM policy for an existing Google Cloud Platform Billing Account.</p>
<p>&gt; <strong>Warning:</strong> Billing accounts have a default user that can be <strong>overwritten</strong>
by use of this resource. The safest alternative is to use multiple <cite>google_billing_account_iam_binding</cite></p>
<blockquote>
<div>resources. If you do use this resource, the best way to be sure that you are
not making dangerous changes is to start by importing your existing policy,
and examining the diff very closely.</div></blockquote>
<dl class="docutils">
<dt>&gt; <strong>Note:</strong> This resource __must <a href="#id1"><span class="problematic" id="id6">not__</span></a> be used in conjunction with</dt>
<dd><cite>google_billing_account_iam_member</cite> or <cite>google_billing_account_iam_binding</cite>
or they will fight over what your policy should be.</dd>
</dl>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <cite>google_iam_policy</cite> data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamPolicy.billing_account_id">
<code class="descname">billing_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.billing.AccountIamPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <cite>google_iam_policy</cite> data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.billing.AccountIamPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
