---
title: Module s3
---

<div class="section" id="s3">
<h1>s3<a class="headerlink" href="#s3" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.s3"></span><dl class="class">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">AccountPublicAccessBlock</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">block_public_acls=None</em>, <em class="sig-param">block_public_policy=None</em>, <em class="sig-param">ignore_public_acls=None</em>, <em class="sig-param">restrict_public_buckets=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages S3 account-level Public Access Block configuration. For more information about these settings, see the <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html">AWS S3 Block Public Access documentation</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Each AWS account may only have one S3 Public Access Block configuration. Multiple configurations of the resource against the same AWS account will cause a perpetual difference.</p>
<p>Advanced usage: To use a custom API endpoint for this resource, use the <cite>``s3control`</cite> endpoint provider configuration &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/index.html#s3control">https://www.terraform.io/docs/providers/aws/index.html#s3control</a>&gt;`_, not the <code class="docutils literal notranslate"><span class="pre">s3</span></code> endpoint provider configuration.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.</p></li>
<li><p><strong>block_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">acl</span> <span class="ow">and</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">acl</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">ACL</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
<span class="o">*</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">request</span> <span class="n">includes</span> <span class="n">an</span> <span class="nb">object</span> <span class="n">ACL</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing bucket policies. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Reject</span> <span class="n">calls</span> <span class="n">to</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">policy</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">bucket</span> <span class="n">policy</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Ignore</span> <span class="nb">all</span> <span class="n">public</span> <span class="n">ACLs</span> <span class="n">on</span> <span class="n">buckets</span> <span class="ow">in</span> <span class="n">this</span> <span class="n">account</span> <span class="ow">and</span> <span class="nb">any</span> <span class="n">objects</span> <span class="n">that</span> <span class="n">they</span> <span class="n">contain</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Only</span> <span class="n">the</span> <span class="n">bucket</span> <span class="n">owner</span> <span class="ow">and</span> <span class="n">AWS</span> <span class="n">Services</span> <span class="n">can</span> <span class="n">access</span> <span class="n">buckets</span> <span class="k">with</span> <span class="n">public</span> <span class="n">policies</span><span class="o">.</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.block_public_acls">
<code class="sig-name descname">block_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.block_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<ul class="simple">
<li><p>PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.</p></li>
<li><p>PUT Object calls will fail if the request includes an object ACL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.block_public_policy">
<code class="sig-name descname">block_public_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.block_public_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing bucket policies. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li><p>Reject calls to PUT Bucket policy if the specified bucket policy allows public access.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.ignore_public_acls">
<code class="sig-name descname">ignore_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.ignore_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li><p>Ignore all public ACLs on buckets in this account and any objects that they contain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.restrict_public_buckets">
<code class="sig-name descname">restrict_public_buckets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.restrict_public_buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
<ul class="simple">
<li><p>Only the bucket owner and AWS Services can access buckets with public policies.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">block_public_acls=None</em>, <em class="sig-param">block_public_policy=None</em>, <em class="sig-param">ignore_public_acls=None</em>, <em class="sig-param">restrict_public_buckets=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountPublicAccessBlock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_id: AWS account ID to configure. Defaults to automatically determined account ID of the this provider AWS provider.
:param pulumi.Input[bool] block_public_acls: Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">acl</span> <span class="ow">and</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">acl</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">ACL</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
<span class="o">*</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">request</span> <span class="n">includes</span> <span class="n">an</span> <span class="nb">object</span> <span class="n">ACL</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing bucket policies. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Reject</span> <span class="n">calls</span> <span class="n">to</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">policy</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">bucket</span> <span class="n">policy</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Ignore</span> <span class="nb">all</span> <span class="n">public</span> <span class="n">ACLs</span> <span class="n">on</span> <span class="n">buckets</span> <span class="ow">in</span> <span class="n">this</span> <span class="n">account</span> <span class="ow">and</span> <span class="nb">any</span> <span class="n">objects</span> <span class="n">that</span> <span class="n">they</span> <span class="n">contain</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Only</span> <span class="n">the</span> <span class="n">bucket</span> <span class="n">owner</span> <span class="ow">and</span> <span class="n">AWS</span> <span class="n">Services</span> <span class="n">can</span> <span class="n">access</span> <span class="n">buckets</span> <span class="k">with</span> <span class="n">public</span> <span class="n">policies</span><span class="o">.</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.AwaitableGetBucketObjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">AwaitableGetBucketObjectResult</code><span class="sig-paren">(</span><em class="sig-param">body=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_length=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_modified=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">range=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">sse_kms_key_id=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">website_redirect_location=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AwaitableGetBucketObjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.AwaitableGetBucketObjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">AwaitableGetBucketObjectsResult</code><span class="sig-paren">(</span><em class="sig-param">bucket=None</em>, <em class="sig-param">common_prefixes=None</em>, <em class="sig-param">delimiter=None</em>, <em class="sig-param">encoding_type=None</em>, <em class="sig-param">fetch_owner=None</em>, <em class="sig-param">keys=None</em>, <em class="sig-param">max_keys=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">start_after=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AwaitableGetBucketObjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.AwaitableGetBucketResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">AwaitableGetBucketResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">bucket_domain_name=None</em>, <em class="sig-param">bucket_regional_domain_name=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">website_domain=None</em>, <em class="sig-param">website_endpoint=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AwaitableGetBucketResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.Bucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">Bucket</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acceleration_status=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">bucket_prefix=None</em>, <em class="sig-param">cors_rules=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">lifecycle_rules=None</em>, <em class="sig-param">loggings=None</em>, <em class="sig-param">object_lock_configuration=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replication_configuration=None</em>, <em class="sig-param">request_payer=None</em>, <em class="sig-param">server_side_encryption_configuration=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">versioning=None</em>, <em class="sig-param">website=None</em>, <em class="sig-param">website_domain=None</em>, <em class="sig-param">website_endpoint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acceleration_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the accelerate configuration of an existing bucket. Can be <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.</p></li>
<li><p><strong>bucket_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique bucket name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">bucket</span></code>.</p></li>
<li><p><strong>cors_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html">Cross-Origin Resource Sharing</a> (documented below).</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are <em>not</em> recoverable.</p></li>
<li><p><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</p></li>
<li><p><strong>lifecycle_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a> (documented below).</p></li>
<li><p><strong>loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A settings of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html">bucket logging</a> (documented below).</p></li>
<li><p><strong>object_lock_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">S3 object locking</a> (documented below)</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html">bucket policy</a> JSON document. Note that if the policy document is not specific enough (but still valid), this provider may view the policy as constantly changing in a deployment. In this case, please make sure you use the verbose/specific version of the policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.</p></li>
<li><p><strong>replication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html">replication configuration</a> (documented below).</p></li>
<li><p><strong>request_payer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies who should bear the cost of Amazon S3 data transfer.
Can be either <code class="docutils literal notranslate"><span class="pre">BucketOwner</span></code> or <code class="docutils literal notranslate"><span class="pre">Requester</span></code>. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a>
developer guide for more information.</p></li>
<li><p><strong>server_side_encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html">server-side encryption configuration</a> (documented below)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.</p></li>
<li><p><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A state of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html">versioning</a> (documented below)</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A website object (documented below).</p></li>
<li><p><strong>website_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p></li>
<li><p><strong>website_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.acceleration_status">
<code class="sig-name descname">acceleration_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.acceleration_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the accelerate configuration of an existing bucket. Can be <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_domain_name">
<code class="sig-name descname">bucket_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket domain name. Will be of format <code class="docutils literal notranslate"><span class="pre">bucketname.s3.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_prefix">
<code class="sig-name descname">bucket_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique bucket name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">bucket</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_regional_domain_name">
<code class="sig-name descname">bucket_regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket region-specific domain name. The bucket domain name including the region name, please refer <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">here</a> for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent <a class="reference external" href="https://forums.aws.amazon.com/thread.jspa?threadID=216814">redirect issues</a> from CloudFront to S3 Origin URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.cors_rules">
<code class="sig-name descname">cors_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.cors_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html">Cross-Origin Resource Sharing</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.lifecycle_rules">
<code class="sig-name descname">lifecycle_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.lifecycle_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.loggings">
<code class="sig-name descname">loggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.loggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A settings of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html">bucket logging</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.object_lock_configuration">
<code class="sig-name descname">object_lock_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.object_lock_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">S3 object locking</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html">bucket policy</a> JSON document. Note that if the policy document is not specific enough (but still valid), this provider may view the policy as constantly changing in a deployment. In this case, please make sure you use the verbose/specific version of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.region" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.replication_configuration">
<code class="sig-name descname">replication_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.replication_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html">replication configuration</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.request_payer">
<code class="sig-name descname">request_payer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.request_payer" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies who should bear the cost of Amazon S3 data transfer.
Can be either <code class="docutils literal notranslate"><span class="pre">BucketOwner</span></code> or <code class="docutils literal notranslate"><span class="pre">Requester</span></code>. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a>
developer guide for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.server_side_encryption_configuration">
<code class="sig-name descname">server_side_encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.server_side_encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html">server-side encryption configuration</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.versioning">
<code class="sig-name descname">versioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>A state of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html">versioning</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website">
<code class="sig-name descname">website</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website" title="Permalink to this definition">¶</a></dt>
<dd><p>A website object (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website_domain">
<code class="sig-name descname">website_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website_endpoint">
<code class="sig-name descname">website_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Bucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acceleration_status=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">bucket_domain_name=None</em>, <em class="sig-param">bucket_prefix=None</em>, <em class="sig-param">bucket_regional_domain_name=None</em>, <em class="sig-param">cors_rules=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">lifecycle_rules=None</em>, <em class="sig-param">loggings=None</em>, <em class="sig-param">object_lock_configuration=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replication_configuration=None</em>, <em class="sig-param">request_payer=None</em>, <em class="sig-param">server_side_encryption_configuration=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">versioning=None</em>, <em class="sig-param">website=None</em>, <em class="sig-param">website_domain=None</em>, <em class="sig-param">website_endpoint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Bucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] acceleration_status: Sets the accelerate configuration of an existing bucket. Can be <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.
:param pulumi.Input[str] acl: The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.
:param pulumi.Input[str] arn: The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.
:param pulumi.Input[str] bucket: The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
:param pulumi.Input[str] bucket_domain_name: The bucket domain name. Will be of format <code class="docutils literal notranslate"><span class="pre">bucketname.s3.amazonaws.com</span></code>.
:param pulumi.Input[str] bucket_prefix: Creates a unique bucket name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">bucket</span></code>.
:param pulumi.Input[str] bucket_regional_domain_name: The bucket region-specific domain name. The bucket domain name including the region name, please refer <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">here</a> for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent <a class="reference external" href="https://forums.aws.amazon.com/thread.jspa?threadID=216814">redirect issues</a> from CloudFront to S3 Origin URL.
:param pulumi.Input[list] cors_rules: A rule of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html">Cross-Origin Resource Sharing</a> (documented below).
:param pulumi.Input[bool] force_destroy: A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are <em>not</em> recoverable.
:param pulumi.Input[str] hosted_zone_id: The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.
:param pulumi.Input[list] lifecycle_rules: A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a> (documented below).
:param pulumi.Input[list] loggings: A settings of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html">bucket logging</a> (documented below).
:param pulumi.Input[dict] object_lock_configuration: A configuration of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">S3 object locking</a> (documented below)
:param pulumi.Input[str] policy: A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html">bucket policy</a> JSON document. Note that if the policy document is not specific enough (but still valid), this provider may view the policy as constantly changing in a deployment. In this case, please make sure you use the verbose/specific version of the policy.
:param pulumi.Input[str] region: If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
:param pulumi.Input[dict] replication_configuration: A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html">replication configuration</a> (documented below).
:param pulumi.Input[str] request_payer: Specifies who should bear the cost of Amazon S3 data transfer.</p>
<blockquote>
<div><p>Can be either <code class="docutils literal notranslate"><span class="pre">BucketOwner</span></code> or <code class="docutils literal notranslate"><span class="pre">Requester</span></code>. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a>
developer guide for more information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>server_side_encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html">server-side encryption configuration</a> (documented below)</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.</p></li>
<li><p><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A state of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html">versioning</a> (documented below)</p>
</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A website object (documented below).</p></li>
<li><p><strong>website_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p></li>
<li><p><strong>website_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Bucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.Bucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketMetric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">BucketMetric</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html">metrics configuration</a> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put metric configuration.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter">Object filtering</a> that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the metrics configuration for the bucket.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put metric configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.filter" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter">Object filtering</a> that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the metrics configuration for the bucket.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] bucket: The name of the bucket to put metric configuration.
:param pulumi.Input[dict] filter: <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter">Object filtering</a> that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
:param pulumi.Input[str] name: Unique identifier of the metrics configuration for the bucket.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketMetric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketMetric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketNotification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">BucketNotification</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">lambda_functions=None</em>, <em class="sig-param">queues=None</em>, <em class="sig-param">topics=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a S3 Bucket Notification Configuration. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">Configuring S3 Event Notifications section in the Amazon S3 Developer Guide</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> S3 Buckets only support a single notification configuration. Declaring multiple <code class="docutils literal notranslate"><span class="pre">s3.BucketNotification</span></code> resources to the same S3 Bucket will cause a perpetual difference in configuration.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put notification configuration.</p></li>
<li><p><strong>lambda_functions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Used to configure notifications to a Lambda Function (documented below).</p></li>
<li><p><strong>queues</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification configuration to SQS Queue (documented below).</p></li>
<li><p><strong>topics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification configuration to SNS Topic (documented below).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put notification configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.lambda_functions">
<code class="sig-name descname">lambda_functions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.lambda_functions" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to configure notifications to a Lambda Function (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.queues">
<code class="sig-name descname">queues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.queues" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification configuration to SQS Queue (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.topics">
<code class="sig-name descname">topics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification configuration to SNS Topic (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketNotification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">lambda_functions=None</em>, <em class="sig-param">queues=None</em>, <em class="sig-param">topics=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketNotification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] bucket: The name of the bucket to put notification configuration.
:param pulumi.Input[list] lambda_functions: Used to configure notifications to a Lambda Function (documented below).
:param pulumi.Input[list] queues: The notification configuration to SQS Queue (documented below).
:param pulumi.Input[list] topics: The notification configuration to SNS Topic (documented below).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketNotification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketNotification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketObject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">BucketObject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">content_base64=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">website_redirect=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket object resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the file in.</p></li>
<li><p><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><strong>content_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p></li>
<li><p><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p></li>
<li><p><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p></li>
<li><p><strong>content_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language the content is in e.g. en-US or en-GB.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to trigger updates. The only meaningful value is <code class="docutils literal notranslate"><span class="pre">${filemd5(&quot;path/to/file&quot;)}</span></code> (this provider 0.11.12 or later) or <code class="docutils literal notranslate"><span class="pre">${md5(file(&quot;path/to/file&quot;))}</span></code> (this provider 0.11.11 or earlier).
This attribute is not compatible with KMS encryption, <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> or <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span> <span class="pre">=</span> <span class="pre">&quot;aws:kms&quot;</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object once it is in the bucket.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified <strong>ARN</strong> of the KMS Key. If using <code class="docutils literal notranslate"><span class="pre">kms.Key</span></code>,
use the exported <code class="docutils literal notranslate"><span class="pre">arn</span></code> attribute:
<code class="docutils literal notranslate"><span class="pre">kms_key_id</span> <span class="pre">=</span> <span class="pre">&quot;${aws_kms_key.foo.arn}&quot;</span></code></p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of keys/values to provision metadata (will be automatically prefixed by <code class="docutils literal notranslate"><span class="pre">x-amz-meta-</span></code>, note that only lowercase label are currently supported by the AWS Go API).</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies server-side encryption of the object in S3. Valid values are “<code class="docutils literal notranslate"><span class="pre">AES256</span></code>” and “<code class="docutils literal notranslate"><span class="pre">aws:kms</span></code>”.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.Asset</em><em>]</em>) – The path to a file that will be read and uploaded as raw bytes for the object content.</p></li>
<li><p><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the desired <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Class</a>
for the object. Can be either “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”, “<code class="docutils literal notranslate"><span class="pre">REDUCED_REDUNDANCY</span></code>”, “<code class="docutils literal notranslate"><span class="pre">ONEZONE_IA</span></code>”, “<code class="docutils literal notranslate"><span class="pre">INTELLIGENT_TIERING</span></code>”, “<code class="docutils literal notranslate"><span class="pre">GLACIER</span></code>”, “<code class="docutils literal notranslate"><span class="pre">DEEP_ARCHIVE</span></code>”, or “<code class="docutils literal notranslate"><span class="pre">STANDARD_IA</span></code>”. Defaults to “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</p></li>
<li><p><strong>website_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a target URL for <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">website redirect</a>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put the file in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.cache_control">
<code class="sig-name descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_base64">
<code class="sig-name descname">content_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_disposition">
<code class="sig-name descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_encoding">
<code class="sig-name descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_language">
<code class="sig-name descname">content_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The language the content is in e.g. en-US or en-GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to trigger updates. The only meaningful value is <code class="docutils literal notranslate"><span class="pre">${filemd5(&quot;path/to/file&quot;)}</span></code> (this provider 0.11.12 or later) or <code class="docutils literal notranslate"><span class="pre">${md5(file(&quot;path/to/file&quot;))}</span></code> (this provider 0.11.11 or earlier).
This attribute is not compatible with KMS encryption, <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> or <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span> <span class="pre">=</span> <span class="pre">&quot;aws:kms&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the object once it is in the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified <strong>ARN</strong> of the KMS Key. If using <code class="docutils literal notranslate"><span class="pre">kms.Key</span></code>,
use the exported <code class="docutils literal notranslate"><span class="pre">arn</span></code> attribute:
<code class="docutils literal notranslate"><span class="pre">kms_key_id</span> <span class="pre">=</span> <span class="pre">&quot;${aws_kms_key.foo.arn}&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of keys/values to provision metadata (will be automatically prefixed by <code class="docutils literal notranslate"><span class="pre">x-amz-meta-</span></code>, note that only lowercase label are currently supported by the AWS Go API).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies server-side encryption of the object in S3. Valid values are “<code class="docutils literal notranslate"><span class="pre">AES256</span></code>” and “<code class="docutils literal notranslate"><span class="pre">aws:kms</span></code>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to a file that will be read and uploaded as raw bytes for the object content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.storage_class">
<code class="sig-name descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the desired <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Class</a>
for the object. Can be either “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”, “<code class="docutils literal notranslate"><span class="pre">REDUCED_REDUNDANCY</span></code>”, “<code class="docutils literal notranslate"><span class="pre">ONEZONE_IA</span></code>”, “<code class="docutils literal notranslate"><span class="pre">INTELLIGENT_TIERING</span></code>”, “<code class="docutils literal notranslate"><span class="pre">GLACIER</span></code>”, “<code class="docutils literal notranslate"><span class="pre">DEEP_ARCHIVE</span></code>”, or “<code class="docutils literal notranslate"><span class="pre">STANDARD_IA</span></code>”. Defaults to “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique version ID value for the object, if bucket versioning
is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.website_redirect">
<code class="sig-name descname">website_redirect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.website_redirect" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a target URL for <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">website redirect</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketObject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">content_base64=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">website_redirect=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketObject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] acl: The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.
:param pulumi.Input[str] bucket: The name of the bucket to put the file in.
:param pulumi.Input[str] cache_control: Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.
:param pulumi.Input[str] content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
:param pulumi.Input[str] content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.
:param pulumi.Input[str] content_disposition: Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.
:param pulumi.Input[str] content_encoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.
:param pulumi.Input[str] content_language: The language the content is in e.g. en-US or en-GB.
:param pulumi.Input[str] content_type: A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
:param pulumi.Input[str] etag: Used to trigger updates. The only meaningful value is <code class="docutils literal notranslate"><span class="pre">${filemd5(&quot;path/to/file&quot;)}</span></code> (this provider 0.11.12 or later) or <code class="docutils literal notranslate"><span class="pre">${md5(file(&quot;path/to/file&quot;))}</span></code> (this provider 0.11.11 or earlier).</p>
<blockquote>
<div><p>This attribute is not compatible with KMS encryption, <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> or <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span> <span class="pre">=</span> <span class="pre">&quot;aws:kms&quot;</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object once it is in the bucket.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified <strong>ARN</strong> of the KMS Key. If using <code class="docutils literal notranslate"><span class="pre">kms.Key</span></code>,
use the exported <code class="docutils literal notranslate"><span class="pre">arn</span></code> attribute:
<code class="docutils literal notranslate"><span class="pre">kms_key_id</span> <span class="pre">=</span> <span class="pre">&quot;${aws_kms_key.foo.arn}&quot;</span></code></p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of keys/values to provision metadata (will be automatically prefixed by <code class="docutils literal notranslate"><span class="pre">x-amz-meta-</span></code>, note that only lowercase label are currently supported by the AWS Go API).</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies server-side encryption of the object in S3. Valid values are “<code class="docutils literal notranslate"><span class="pre">AES256</span></code>” and “<code class="docutils literal notranslate"><span class="pre">aws:kms</span></code>”.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.Asset</em><em>]</em>) – The path to a file that will be read and uploaded as raw bytes for the object content.</p></li>
<li><p><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the desired <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Class</a>
for the object. Can be either “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”, “<code class="docutils literal notranslate"><span class="pre">REDUCED_REDUNDANCY</span></code>”, “<code class="docutils literal notranslate"><span class="pre">ONEZONE_IA</span></code>”, “<code class="docutils literal notranslate"><span class="pre">INTELLIGENT_TIERING</span></code>”, “<code class="docutils literal notranslate"><span class="pre">GLACIER</span></code>”, “<code class="docutils literal notranslate"><span class="pre">DEEP_ARCHIVE</span></code>”, or “<code class="docutils literal notranslate"><span class="pre">STANDARD_IA</span></code>”. Defaults to “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique version ID value for the object, if bucket versioning
is enabled.</p></li>
<li><p><strong>website_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies a target URL for <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">website redirect</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketObject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketObject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">BucketPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a policy to an S3 bucket resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to which to apply the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The text of the policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPolicy.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to which to apply the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPolicy.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The text of the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] bucket: The name of the bucket to which to apply the policy.
:param pulumi.Input[str] policy: The text of the policy.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPublicAccessBlock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">BucketPublicAccessBlock</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">block_public_acls=None</em>, <em class="sig-param">block_public_policy=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">ignore_public_acls=None</em>, <em class="sig-param">restrict_public_buckets=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html">AWS S3 Block Public Access documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>block_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">acl</span> <span class="ow">and</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">acl</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">ACL</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
<span class="o">*</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">request</span> <span class="n">includes</span> <span class="n">an</span> <span class="nb">object</span> <span class="n">ACL</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the existing bucket policy. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Reject</span> <span class="n">calls</span> <span class="n">to</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">policy</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">bucket</span> <span class="n">policy</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 Bucket to which this Public Access Block configuration should be applied.</p></li>
<li><p><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Ignore</span> <span class="n">public</span> <span class="n">ACLs</span> <span class="n">on</span> <span class="n">this</span> <span class="n">bucket</span> <span class="ow">and</span> <span class="nb">any</span> <span class="n">objects</span> <span class="n">that</span> <span class="n">it</span> <span class="n">contains</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Only</span> <span class="n">the</span> <span class="n">bucket</span> <span class="n">owner</span> <span class="ow">and</span> <span class="n">AWS</span> <span class="n">Services</span> <span class="n">can</span> <span class="n">access</span> <span class="n">this</span> <span class="n">buckets</span> <span class="k">if</span> <span class="n">it</span> <span class="n">has</span> <span class="n">a</span> <span class="n">public</span> <span class="n">policy</span><span class="o">.</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.block_public_acls">
<code class="sig-name descname">block_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.block_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<ul class="simple">
<li><p>PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.</p></li>
<li><p>PUT Object calls will fail if the request includes an object ACL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.block_public_policy">
<code class="sig-name descname">block_public_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.block_public_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the existing bucket policy. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li><p>Reject calls to PUT Bucket policy if the specified bucket policy allows public access.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 Bucket to which this Public Access Block configuration should be applied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.ignore_public_acls">
<code class="sig-name descname">ignore_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.ignore_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li><p>Ignore public ACLs on this bucket and any objects that it contains.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.restrict_public_buckets">
<code class="sig-name descname">restrict_public_buckets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.restrict_public_buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
<ul class="simple">
<li><p>Only the bucket owner and AWS Services can access this buckets if it has a public policy.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">block_public_acls=None</em>, <em class="sig-param">block_public_policy=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">ignore_public_acls=None</em>, <em class="sig-param">restrict_public_buckets=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketPublicAccessBlock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] block_public_acls: Whether Amazon S3 should block public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">acl</span> <span class="ow">and</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">acl</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">ACL</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
<span class="o">*</span> <span class="n">PUT</span> <span class="n">Object</span> <span class="n">calls</span> <span class="n">will</span> <span class="n">fail</span> <span class="k">if</span> <span class="n">the</span> <span class="n">request</span> <span class="n">includes</span> <span class="n">an</span> <span class="nb">object</span> <span class="n">ACL</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the existing bucket policy. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Reject</span> <span class="n">calls</span> <span class="n">to</span> <span class="n">PUT</span> <span class="n">Bucket</span> <span class="n">policy</span> <span class="k">if</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">bucket</span> <span class="n">policy</span> <span class="n">allows</span> <span class="n">public</span> <span class="n">access</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 Bucket to which this Public Access Block configuration should be applied.</p></li>
<li><p><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Ignore</span> <span class="n">public</span> <span class="n">ACLs</span> <span class="n">on</span> <span class="n">this</span> <span class="n">bucket</span> <span class="ow">and</span> <span class="nb">any</span> <span class="n">objects</span> <span class="n">that</span> <span class="n">it</span> <span class="n">contains</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Only</span> <span class="n">the</span> <span class="n">bucket</span> <span class="n">owner</span> <span class="ow">and</span> <span class="n">AWS</span> <span class="n">Services</span> <span class="n">can</span> <span class="n">access</span> <span class="n">this</span> <span class="n">buckets</span> <span class="k">if</span> <span class="n">it</span> <span class="n">has</span> <span class="n">a</span> <span class="n">public</span> <span class="n">policy</span><span class="o">.</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.GetBucketObjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">GetBucketObjectResult</code><span class="sig-paren">(</span><em class="sig-param">body=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_length=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_modified=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">range=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">sse_kms_key_id=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">website_redirect_location=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucketObject.</p>
<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.body">
<code class="sig-name descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Object data (see <strong>limitations above</strong> to understand cases in which this field is actually available)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.cache_control">
<code class="sig-name descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_disposition">
<code class="sig-name descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_encoding">
<code class="sig-name descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_language">
<code class="sig-name descname">content_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The language the content is in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_length">
<code class="sig-name descname">content_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the body in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.etag" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://en.wikipedia.org/wiki/HTTP_ETag">ETag</a> generated for the object (an MD5 sum of the object content in case it’s not encrypted)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.expiration">
<code class="sig-name descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>If the object expiration is configured (see <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a>), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.expires">
<code class="sig-name descname">expires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.expires" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time at which the object is no longer cacheable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.last_modified">
<code class="sig-name descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>Last modified date of the object in RFC1123 format (e.g. <code class="docutils literal notranslate"><span class="pre">Mon,</span> <span class="pre">02</span> <span class="pre">Jan</span> <span class="pre">2006</span> <span class="pre">15:04:05</span> <span class="pre">MST</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of metadata stored with the object in S3</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.sse_kms_key_id">
<code class="sig-name descname">sse_kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.sse_kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.storage_class">
<code class="sig-name descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage class</a> information of the object. Available for all objects except for <code class="docutils literal notranslate"><span class="pre">Standard</span></code> storage class objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version ID of the object returned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.website_redirect_location">
<code class="sig-name descname">website_redirect_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.website_redirect_location" title="Permalink to this definition">¶</a></dt>
<dd><p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.GetBucketObjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">GetBucketObjectsResult</code><span class="sig-paren">(</span><em class="sig-param">bucket=None</em>, <em class="sig-param">common_prefixes=None</em>, <em class="sig-param">delimiter=None</em>, <em class="sig-param">encoding_type=None</em>, <em class="sig-param">fetch_owner=None</em>, <em class="sig-param">keys=None</em>, <em class="sig-param">max_keys=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">start_after=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucketObjects.</p>
<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectsResult.common_prefixes">
<code class="sig-name descname">common_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectsResult.common_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of any keys between <code class="docutils literal notranslate"><span class="pre">prefix</span></code> and the next occurrence of <code class="docutils literal notranslate"><span class="pre">delimiter</span></code> (i.e., similar to subdirectories of the <code class="docutils literal notranslate"><span class="pre">prefix</span></code> “directory”); the list is only returned when you specify <code class="docutils literal notranslate"><span class="pre">delimiter</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectsResult.keys">
<code class="sig-name descname">keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectsResult.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>List of strings representing object keys</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectsResult.owners">
<code class="sig-name descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectsResult.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>List of strings representing object owner IDs (see <code class="docutils literal notranslate"><span class="pre">fetch_owner</span></code> above)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.GetBucketResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">GetBucketResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">bucket_domain_name=None</em>, <em class="sig-param">bucket_regional_domain_name=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">website_domain=None</em>, <em class="sig-param">website_endpoint=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucket.</p>
<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.bucket_domain_name">
<code class="sig-name descname">bucket_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.bucket_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket domain name. Will be of format <code class="docutils literal notranslate"><span class="pre">bucketname.s3.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.bucket_regional_domain_name">
<code class="sig-name descname">bucket_regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.bucket_regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket region-specific domain name. The bucket domain name including the region name, please refer <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">here</a> for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent <a class="reference external" href="https://forums.aws.amazon.com/thread.jspa?threadID=216814">redirect issues</a> from CloudFront to S3 Origin URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region this bucket resides in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.website_domain">
<code class="sig-name descname">website_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.website_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.website_endpoint">
<code class="sig-name descname">website_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.website_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.Inventory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">Inventory</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">included_object_versions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">optional_fields=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html">inventory configuration</a> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket configuration where inventory results are published (documented below).</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Destination bucket where inventory list files are written (documented below).</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the inventory is enabled or disabled.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Object filtering that accepts a prefix (documented below).</p></li>
<li><p><strong>included_object_versions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Object filtering that accepts a prefix (documented below). Can be <code class="docutils literal notranslate"><span class="pre">All</span></code> or <code class="docutils literal notranslate"><span class="pre">Current</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the inventory configuration for the bucket.</p></li>
<li><p><strong>optional_fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains the optional fields that are included in the inventory results.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains the frequency for generating inventory results (documented below).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket configuration where inventory results are published (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination bucket where inventory list files are written (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the inventory is enabled or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Object filtering that accepts a prefix (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.included_object_versions">
<code class="sig-name descname">included_object_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.included_object_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Object filtering that accepts a prefix (documented below). Can be <code class="docutils literal notranslate"><span class="pre">All</span></code> or <code class="docutils literal notranslate"><span class="pre">Current</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the inventory configuration for the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.optional_fields">
<code class="sig-name descname">optional_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.optional_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the optional fields that are included in the inventory results.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.schedule">
<code class="sig-name descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the frequency for generating inventory results (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Inventory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">included_object_versions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">optional_fields=None</em>, <em class="sig-param">schedule=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Inventory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] bucket: The S3 bucket configuration where inventory results are published (documented below).
:param pulumi.Input[dict] destination: Destination bucket where inventory list files are written (documented below).
:param pulumi.Input[bool] enabled: Specifies whether the inventory is enabled or disabled.
:param pulumi.Input[dict] filter: Object filtering that accepts a prefix (documented below).
:param pulumi.Input[str] included_object_versions: Object filtering that accepts a prefix (documented below). Can be <code class="docutils literal notranslate"><span class="pre">All</span></code> or <code class="docutils literal notranslate"><span class="pre">Current</span></code>.
:param pulumi.Input[str] name: Unique identifier of the inventory configuration for the bucket.
:param pulumi.Input[list] optional_fields: Contains the optional fields that are included in the inventory results.
:param pulumi.Input[dict] schedule: Contains the frequency for generating inventory results (documented below).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Inventory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.Inventory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.get_bucket">
<code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">get_bucket</code><span class="sig-paren">(</span><em class="sig-param">bucket=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.get_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific S3 bucket.</p>
<p>This resource may prove useful when setting up a Route53 record, or an origin for a CloudFront
Distribution.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.s3.get_bucket_object">
<code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">get_bucket_object</code><span class="sig-paren">(</span><em class="sig-param">bucket=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">range=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.get_bucket_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 object data source allows access to the metadata and
<em>optionally</em> (see below) content of an object stored inside S3 bucket.</p>
<blockquote>
<div><p><strong>Note:</strong> The content of an object (<code class="docutils literal notranslate"><span class="pre">body</span></code> field) is available only for objects which have a human-readable <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> (<code class="docutils literal notranslate"><span class="pre">text/*</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>). This is to prevent printing unsafe characters and potentially downloading large amount of data which would be thrown away in favour of metadata.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_object.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_object.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.s3.get_bucket_objects">
<code class="sig-prename descclassname">pulumi_aws.s3.</code><code class="sig-name descname">get_bucket_objects</code><span class="sig-paren">(</span><em class="sig-param">bucket=None</em>, <em class="sig-param">delimiter=None</em>, <em class="sig-param">encoding_type=None</em>, <em class="sig-param">fetch_owner=None</em>, <em class="sig-param">max_keys=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">start_after=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.get_bucket_objects" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_objects.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_objects.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
