<div class="section" id="module-pulumi_aws.macie">
<span id="macie"></span><h1>macie<a class="headerlink" href="#module-pulumi_aws.macie" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.macie.MemberAccountAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.macie.</code><code class="descname">MemberAccountAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>member_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an AWS account with Amazon Macie as a member account.</p>
<p>&gt; <strong>NOTE:</strong> Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](<a class="reference external" href="https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable">https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that you want to associate with Amazon Macie as a member account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.macie.MemberAccountAssociation.member_account_id">
<code class="descname">member_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.member_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that you want to associate with Amazon Macie as a member account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.macie.MemberAccountAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.macie.MemberAccountAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.macie.S3BucketAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.macie.</code><code class="descname">S3BucketAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>bucket_name=None</em>, <em>classification_type=None</em>, <em>member_account_id=None</em>, <em>prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an S3 resource with Amazon Macie for monitoring and data classification.</p>
<p>&gt; <strong>NOTE:</strong> Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](<a class="reference external" href="https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable">https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket that you want to associate with Amazon Macie.</li>
<li><strong>classification_type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of how Amazon Macie classifies the S3 objects.</li>
<li><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If <cite>member_account_id</cite> isn’t specified, the action associates specified S3 resources with Macie for the current master account.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Object key prefix identifying one or more S3 objects to which the association applies.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.bucket_name">
<code class="descname">bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the S3 bucket that you want to associate with Amazon Macie.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.classification_type">
<code class="descname">classification_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.classification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of how Amazon Macie classifies the S3 objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.member_account_id">
<code class="descname">member_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.member_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If <cite>member_account_id</cite> isn’t specified, the action associates specified S3 resources with Macie for the current master account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.prefix">
<code class="descname">prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Object key prefix identifying one or more S3 objects to which the association applies.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.macie.S3BucketAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.macie.S3BucketAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
