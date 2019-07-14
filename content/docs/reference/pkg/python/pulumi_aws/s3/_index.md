---
---

<div class="section" id="s3">
<h1>s3<a class="headerlink" href="#s3" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.s3"></span><dl class="class">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">AccountPublicAccessBlock</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>block_public_acls=None</em>, <em>block_public_policy=None</em>, <em>ignore_public_acls=None</em>, <em>restrict_public_buckets=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AccountPublicAccessBlock resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>block_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing bucket policies. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_account_public_access_block.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.block_public_acls">
<code class="descname">block_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.block_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<ul class="simple">
<li>PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.</li>
<li>PUT Object calls will fail if the request includes an object ACL.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.block_public_policy">
<code class="descname">block_public_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.block_public_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing bucket policies. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li>Reject calls to PUT Bucket policy if the specified bucket policy allows public access.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.ignore_public_acls">
<code class="descname">ignore_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.ignore_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li>Ignore all public ACLs on buckets in this account and any objects that they contain.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.restrict_public_buckets">
<code class="descname">restrict_public_buckets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.restrict_public_buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
<ul class="simple">
<li>Only the bucket owner and AWS Services can access buckets with public policies.</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.AccountPublicAccessBlock.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.AccountPublicAccessBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.Bucket">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">Bucket</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>acceleration_status=None</em>, <em>acl=None</em>, <em>arn=None</em>, <em>bucket=None</em>, <em>bucket_prefix=None</em>, <em>cors_rules=None</em>, <em>force_destroy=None</em>, <em>hosted_zone_id=None</em>, <em>lifecycle_rules=None</em>, <em>loggings=None</em>, <em>object_lock_configuration=None</em>, <em>policy=None</em>, <em>region=None</em>, <em>replication_configuration=None</em>, <em>request_payer=None</em>, <em>server_side_encryption_configuration=None</em>, <em>tags=None</em>, <em>versioning=None</em>, <em>website=None</em>, <em>website_domain=None</em>, <em>website_endpoint=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>acceleration_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the accelerate configuration of an existing bucket. Can be <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</li>
<li><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.</li>
<li><strong>bucket_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique bucket name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">bucket</span></code>.</li>
<li><strong>cors_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html">Cross-Origin Resource Sharing</a> (documented below).</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are <em>not</em> recoverable.</li>
<li><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</li>
<li><strong>lifecycle_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a> (documented below).</li>
<li><strong>loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A settings of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html">bucket logging</a> (documented below).</li>
<li><strong>object_lock_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">S3 object locking</a> (documented below)</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.</li>
<li><strong>replication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html">replication configuration</a> (documented below).</li>
<li><strong>request_payer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies who should bear the cost of Amazon S3 data transfer.
Can be either <code class="docutils literal notranslate"><span class="pre">BucketOwner</span></code> or <code class="docutils literal notranslate"><span class="pre">Requester</span></code>. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a>
developer guide for more information.</li>
<li><strong>server_side_encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html">server-side encryption configuration</a> (documented below)</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.</li>
<li><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A state of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html">versioning</a> (documented below)</li>
<li><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A website object (documented below).</li>
<li><strong>website_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</li>
<li><strong>website_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.acceleration_status">
<code class="descname">acceleration_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.acceleration_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the accelerate configuration of an existing bucket. Can be <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.acl">
<code class="descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_domain_name">
<code class="descname">bucket_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket domain name. Will be of format <code class="docutils literal notranslate"><span class="pre">bucketname.s3.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_prefix">
<code class="descname">bucket_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique bucket name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">bucket</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.bucket_regional_domain_name">
<code class="descname">bucket_regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.bucket_regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket region-specific domain name. The bucket domain name including the region name, please refer <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">here</a> for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent <a class="reference external" href="https://forums.aws.amazon.com/thread.jspa?threadID=216814">redirect issues</a> from CloudFront to S3 Origin URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.cors_rules">
<code class="descname">cors_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.cors_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html">Cross-Origin Resource Sharing</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.lifecycle_rules">
<code class="descname">lifecycle_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.lifecycle_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.loggings">
<code class="descname">loggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.loggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A settings of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html">bucket logging</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.object_lock_configuration">
<code class="descname">object_lock_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.object_lock_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html">S3 object locking</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.region" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.replication_configuration">
<code class="descname">replication_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.replication_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html">replication configuration</a> (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.request_payer">
<code class="descname">request_payer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.request_payer" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies who should bear the cost of Amazon S3 data transfer.
Can be either <code class="docutils literal notranslate"><span class="pre">BucketOwner</span></code> or <code class="docutils literal notranslate"><span class="pre">Requester</span></code>. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html">Requester Pays Buckets</a>
developer guide for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.server_side_encryption_configuration">
<code class="descname">server_side_encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.server_side_encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html">server-side encryption configuration</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.versioning">
<code class="descname">versioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>A state of <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html">versioning</a> (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website">
<code class="descname">website</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website" title="Permalink to this definition">¶</a></dt>
<dd><p>A website object (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website_domain">
<code class="descname">website_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Bucket.website_endpoint">
<code class="descname">website_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Bucket.website_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Bucket.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.Bucket.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Bucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketMetric">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">BucketMetric</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>filter=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html">metrics configuration</a> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put metric configuration.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter">Object filtering</a> that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the metrics configuration for the bucket.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_metric.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put metric configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.filter" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter">Object filtering</a> that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketMetric.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the metrics configuration for the bucket.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketMetric.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketMetric.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketNotification">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">BucketNotification</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>lambda_functions=None</em>, <em>queues=None</em>, <em>topics=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a S3 Bucket Notification Configuration. For additional information, see the <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">Configuring S3 Event Notifications section in the Amazon S3 Developer Guide</a>.</p>
<blockquote>
<div><strong>NOTE:</strong> S3 Buckets only support a single notification configuration. Declaring multiple <code class="docutils literal notranslate"><span class="pre">aws_s3_bucket_notification</span></code> resources to the same S3 Bucket will cause a perpetual difference in configuration.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put notification configuration.</li>
<li><strong>lambda_functions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Used to configure notifications to a Lambda Function (documented below).</li>
<li><strong>queues</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification configuration to SQS Queue (documented below).</li>
<li><strong>topics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification configuration to SNS Topic (documented below).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put notification configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.lambda_functions">
<code class="descname">lambda_functions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.lambda_functions" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to configure notifications to a Lambda Function (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.queues">
<code class="descname">queues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.queues" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification configuration to SQS Queue (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketNotification.topics">
<code class="descname">topics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification configuration to SNS Topic (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketNotification.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketNotification.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketNotification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketObject">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">BucketObject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>acl=None</em>, <em>bucket=None</em>, <em>cache_control=None</em>, <em>content=None</em>, <em>content_base64=None</em>, <em>content_disposition=None</em>, <em>content_encoding=None</em>, <em>content_language=None</em>, <em>content_type=None</em>, <em>etag=None</em>, <em>key=None</em>, <em>kms_key_id=None</em>, <em>server_side_encryption=None</em>, <em>source=None</em>, <em>storage_class=None</em>, <em>tags=None</em>, <em>website_redirect=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket object resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the file in.</li>
<li><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</li>
<li><strong>content_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</li>
<li><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</li>
<li><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</li>
<li><strong>content_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language the content is in e.g. en-US or en-GB.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object once it is in the bucket.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified <strong>ARN</strong> of the KMS Key. If using <code class="docutils literal notranslate"><span class="pre">aws_kms_key</span></code>,
use the exported <code class="docutils literal notranslate"><span class="pre">arn</span></code> attribute:
<code class="docutils literal notranslate"><span class="pre">kms_key_id</span> <span class="pre">=</span> <span class="pre">&quot;${aws_kms_key.foo.arn}&quot;</span></code></li>
<li><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies server-side encryption of the object in S3. Valid values are “<code class="docutils literal notranslate"><span class="pre">AES256</span></code>” and “<code class="docutils literal notranslate"><span class="pre">aws:kms</span></code>”.</li>
<li><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.Asset</em><em>]</em>) – The path to a file that will be read and uploaded as raw bytes for the object content.</li>
<li><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the desired <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Class</a>
for the object. Can be either “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”, “<code class="docutils literal notranslate"><span class="pre">REDUCED_REDUNDANCY</span></code>”, “<code class="docutils literal notranslate"><span class="pre">ONEZONE_IA</span></code>”, “<code class="docutils literal notranslate"><span class="pre">INTELLIGENT_TIERING</span></code>”, “<code class="docutils literal notranslate"><span class="pre">GLACIER</span></code>”, “<code class="docutils literal notranslate"><span class="pre">DEEP_ARCHIVE</span></code>”, or “<code class="docutils literal notranslate"><span class="pre">STANDARD_IA</span></code>”. Defaults to “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
<li><strong>website_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a target URL for <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">website redirect</a>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_object.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.acl">
<code class="descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">canned ACL</a> to apply. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put the file in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.cache_control">
<code class="descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_base64">
<code class="descname">content_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_disposition">
<code class="descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_encoding">
<code class="descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_language">
<code class="descname">content_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The language the content is in e.g. en-US or en-GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the object once it is in the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified <strong>ARN</strong> of the KMS Key. If using <code class="docutils literal notranslate"><span class="pre">aws_kms_key</span></code>,
use the exported <code class="docutils literal notranslate"><span class="pre">arn</span></code> attribute:
<code class="docutils literal notranslate"><span class="pre">kms_key_id</span> <span class="pre">=</span> <span class="pre">&quot;${aws_kms_key.foo.arn}&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.server_side_encryption">
<code class="descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies server-side encryption of the object in S3. Valid values are “<code class="docutils literal notranslate"><span class="pre">AES256</span></code>” and “<code class="docutils literal notranslate"><span class="pre">aws:kms</span></code>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.source">
<code class="descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to a file that will be read and uploaded as raw bytes for the object content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.storage_class">
<code class="descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the desired <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage Class</a>
for the object. Can be either “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”, “<code class="docutils literal notranslate"><span class="pre">REDUCED_REDUNDANCY</span></code>”, “<code class="docutils literal notranslate"><span class="pre">ONEZONE_IA</span></code>”, “<code class="docutils literal notranslate"><span class="pre">INTELLIGENT_TIERING</span></code>”, “<code class="docutils literal notranslate"><span class="pre">GLACIER</span></code>”, “<code class="docutils literal notranslate"><span class="pre">DEEP_ARCHIVE</span></code>”, or “<code class="docutils literal notranslate"><span class="pre">STANDARD_IA</span></code>”. Defaults to “<code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.version_id">
<code class="descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique version ID value for the object, if bucket versioning
is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketObject.website_redirect">
<code class="descname">website_redirect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketObject.website_redirect" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a target URL for <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html">website redirect</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketObject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketObject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">BucketPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a policy to an S3 bucket resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to which to apply the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPolicy.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to which to apply the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPublicAccessBlock">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">BucketPublicAccessBlock</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>block_public_acls=None</em>, <em>block_public_policy=None</em>, <em>bucket=None</em>, <em>ignore_public_acls=None</em>, <em>restrict_public_buckets=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html">AWS S3 Block Public Access documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>block_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>block_public_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should block public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the existing bucket policy. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 Bucket to which this Public Access Block configuration should be applied.</li>
<li><strong>ignore_public_acls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>restrict_public_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.block_public_acls">
<code class="descname">block_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.block_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect existing policies or ACLs. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes the following behavior:</p>
<ul class="simple">
<li>PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.</li>
<li>PUT Object calls will fail if the request includes an object ACL.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.block_public_policy">
<code class="descname">block_public_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.block_public_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should block public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the existing bucket policy. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li>Reject calls to PUT Bucket policy if the specified bucket policy allows public access.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 Bucket to which this Public Access Block configuration should be applied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.ignore_public_acls">
<code class="descname">ignore_public_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.ignore_public_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the persistence of any existing ACLs and doesn’t prevent new public ACLs from being set. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code> causes Amazon S3 to:</p>
<ul class="simple">
<li>Ignore public ACLs on this bucket and any objects that it contains.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.restrict_public_buckets">
<code class="descname">restrict_public_buckets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.restrict_public_buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>:</p>
<ul class="simple">
<li>Only the bucket owner and AWS Services can access this buckets if it has a public policy.</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.BucketPublicAccessBlock.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.BucketPublicAccessBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.GetBucketObjectResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">GetBucketObjectResult</code><span class="sig-paren">(</span><em>body=None</em>, <em>bucket=None</em>, <em>cache_control=None</em>, <em>content_disposition=None</em>, <em>content_encoding=None</em>, <em>content_language=None</em>, <em>content_length=None</em>, <em>content_type=None</em>, <em>etag=None</em>, <em>expiration=None</em>, <em>expires=None</em>, <em>key=None</em>, <em>last_modified=None</em>, <em>metadata=None</em>, <em>range=None</em>, <em>server_side_encryption=None</em>, <em>sse_kms_key_id=None</em>, <em>storage_class=None</em>, <em>tags=None</em>, <em>version_id=None</em>, <em>website_redirect_location=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucketObject.</p>
<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Object data (see <strong>limitations above</strong> to understand cases in which this field is actually available)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.cache_control">
<code class="descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_disposition">
<code class="descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_encoding">
<code class="descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_language">
<code class="descname">content_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The language the content is in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_length">
<code class="descname">content_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the body in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.etag" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://en.wikipedia.org/wiki/HTTP_ETag">ETag</a> generated for the object (an MD5 sum of the object content in case it’s not encrypted)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.expiration">
<code class="descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>If the object expiration is configured (see <a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html">object lifecycle management</a>), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.expires">
<code class="descname">expires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.expires" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time at which the object is no longer cacheable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.last_modified">
<code class="descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>Last modified date of the object in RFC1123 format (e.g. <code class="docutils literal notranslate"><span class="pre">Mon,</span> <span class="pre">02</span> <span class="pre">Jan</span> <span class="pre">2006</span> <span class="pre">15:04:05</span> <span class="pre">MST</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of metadata stored with the object in S3</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.server_side_encryption">
<code class="descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.sse_kms_key_id">
<code class="descname">sse_kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.sse_kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.storage_class">
<code class="descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html">Storage class</a> information of the object. Available for all objects except for <code class="docutils literal notranslate"><span class="pre">Standard</span></code> storage class objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.version_id">
<code class="descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version ID of the object returned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.website_redirect_location">
<code class="descname">website_redirect_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.website_redirect_location" title="Permalink to this definition">¶</a></dt>
<dd><p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketObjectResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketObjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.GetBucketResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">GetBucketResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>bucket=None</em>, <em>bucket_domain_name=None</em>, <em>bucket_regional_domain_name=None</em>, <em>hosted_zone_id=None</em>, <em>region=None</em>, <em>website_domain=None</em>, <em>website_endpoint=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucket.</p>
<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the bucket. Will be of format <code class="docutils literal notranslate"><span class="pre">arn:aws:s3:::bucketname</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.bucket_domain_name">
<code class="descname">bucket_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.bucket_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket domain name. Will be of format <code class="docutils literal notranslate"><span class="pre">bucketname.s3.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.bucket_regional_domain_name">
<code class="descname">bucket_regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.bucket_regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket region-specific domain name. The bucket domain name including the region name, please refer <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">here</a> for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent <a class="reference external" href="https://forums.aws.amazon.com/thread.jspa?threadID=216814">redirect issues</a> from CloudFront to S3 Origin URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints">Route 53 Hosted Zone ID</a> for this bucket’s region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region this bucket resides in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.website_domain">
<code class="descname">website_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.website_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.website_endpoint">
<code class="descname">website_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.website_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.GetBucketResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.GetBucketResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.s3.Inventory">
<em class="property">class </em><code class="descclassname">pulumi_aws.s3.</code><code class="descname">Inventory</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>destination=None</em>, <em>enabled=None</em>, <em>filter=None</em>, <em>included_object_versions=None</em>, <em>name=None</em>, <em>optional_fields=None</em>, <em>schedule=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a S3 bucket <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html">inventory configuration</a> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket configuration where inventory results are published (documented below).</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Destination bucket where inventory list files are written (documented below).</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the inventory is enabled or disabled.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Object filtering that accepts a prefix (documented below).</li>
<li><strong>included_object_versions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Object filtering that accepts a prefix (documented below). Can be <code class="docutils literal notranslate"><span class="pre">All</span></code> or <code class="docutils literal notranslate"><span class="pre">Current</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the inventory configuration for the bucket.</li>
<li><strong>optional_fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains the optional fields that are included in the inventory results.</li>
<li><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains the frequency for generating inventory results (documented below).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket configuration where inventory results are published (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination bucket where inventory list files are written (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the inventory is enabled or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Object filtering that accepts a prefix (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.included_object_versions">
<code class="descname">included_object_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.included_object_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Object filtering that accepts a prefix (documented below). Can be <code class="docutils literal notranslate"><span class="pre">All</span></code> or <code class="docutils literal notranslate"><span class="pre">Current</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the inventory configuration for the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.optional_fields">
<code class="descname">optional_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.optional_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the optional fields that are included in the inventory results.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.s3.Inventory.schedule">
<code class="descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.s3.Inventory.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the frequency for generating inventory results (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.s3.Inventory.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.s3.Inventory.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.Inventory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.s3.get_bucket">
<code class="descclassname">pulumi_aws.s3.</code><code class="descname">get_bucket</code><span class="sig-paren">(</span><em>bucket=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.get_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific S3 bucket.</p>
<p>This resource may prove useful when setting up a Route53 record, or an origin for a CloudFront
Distribution.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.s3.get_bucket_object">
<code class="descclassname">pulumi_aws.s3.</code><code class="descname">get_bucket_object</code><span class="sig-paren">(</span><em>bucket=None</em>, <em>key=None</em>, <em>range=None</em>, <em>tags=None</em>, <em>version_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.s3.get_bucket_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 object data source allows access to the metadata and
<em>optionally</em> (see below) content of an object stored inside S3 bucket.</p>
<blockquote>
<div><p><strong>Note:</strong> The content of an object (<code class="docutils literal notranslate"><span class="pre">body</span></code> field) is available only for objects which have a human-readable <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> (<code class="docutils literal notranslate"><span class="pre">text/*</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>). This is to prevent printing unsafe characters and potentially downloading large amount of data which would be thrown away in favour of metadata.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_object.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/s3_bucket_object.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
