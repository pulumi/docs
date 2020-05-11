---
title: Module macie
title_tag: Module macie | Package pulumi_aws | Python SDK
linktitle: macie
notitle: true
---

<div class="section" id="macie">
<h1>macie<a class="headerlink" href="#macie" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.macie"></span><dl class="py class">
<dt id="pulumi_aws.macie.MemberAccountAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.macie.</code><code class="sig-name descname">MemberAccountAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an AWS account with Amazon Macie as a member account.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Before using Amazon Macie for the first time it must be enabled manually. Instructions are <a class="reference external" href="https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable">here</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">macie</span><span class="o">.</span><span class="n">MemberAccountAssociation</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">member_account_id</span><span class="o">=</span><span class="s2">&quot;123456789012&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that you want to associate with Amazon Macie as a member account.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.macie.MemberAccountAssociation.member_account_id">
<code class="sig-name descname">member_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.member_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that you want to associate with Amazon Macie as a member account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.macie.MemberAccountAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MemberAccountAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that you want to associate with Amazon Macie as a member account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.macie.MemberAccountAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.macie.MemberAccountAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.MemberAccountAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.macie.S3BucketAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.macie.</code><code class="sig-name descname">S3BucketAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classification_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an S3 resource with Amazon Macie for monitoring and data classification.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Before using Amazon Macie for the first time it must be enabled manually. Instructions are <a class="reference external" href="https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable">here</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">macie</span><span class="o">.</span><span class="n">S3BucketAssociation</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">bucket_name</span><span class="o">=</span><span class="s2">&quot;tf-macie-example&quot;</span><span class="p">,</span>
    <span class="n">classification_type</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;oneTime&quot;</span><span class="p">:</span> <span class="s2">&quot;FULL&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;data&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket that you want to associate with Amazon Macie.</p></li>
<li><p><strong>classification_type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of how Amazon Macie classifies the S3 objects.</p></li>
<li><p><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If <code class="docutils literal notranslate"><span class="pre">member_account_id</span></code> isn’t specified, the action associates specified S3 resources with Macie for the current master account.</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Object key prefix identifying one or more S3 objects to which the association applies.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>classification_type</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continuous</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
The only valid value is the default value, <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code> indicating that Macie only classifies objects that are added after the association was created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.bucket_name">
<code class="sig-name descname">bucket_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the S3 bucket that you want to associate with Amazon Macie.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.classification_type">
<code class="sig-name descname">classification_type</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.classification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of how Amazon Macie classifies the S3 objects.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continuous</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
The only valid value is the default value, <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code> indicating that Macie only classifies objects that are added after the association was created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.member_account_id">
<code class="sig-name descname">member_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.member_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If <code class="docutils literal notranslate"><span class="pre">member_account_id</span></code> isn’t specified, the action associates specified S3 resources with Macie for the current master account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.macie.S3BucketAssociation.prefix">
<code class="sig-name descname">prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Object key prefix identifying one or more S3 objects to which the association applies.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.macie.S3BucketAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">classification_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing S3BucketAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket that you want to associate with Amazon Macie.</p></li>
<li><p><strong>classification_type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of how Amazon Macie classifies the S3 objects.</p></li>
<li><p><strong>member_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If <code class="docutils literal notranslate"><span class="pre">member_account_id</span></code> isn’t specified, the action associates specified S3 resources with Macie for the current master account.</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Object key prefix identifying one or more S3 objects to which the association applies.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>classification_type</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continuous</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
The only valid value is the default value, <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code> indicating that Macie only classifies objects that are added after the association was created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.macie.S3BucketAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.macie.S3BucketAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.macie.S3BucketAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
