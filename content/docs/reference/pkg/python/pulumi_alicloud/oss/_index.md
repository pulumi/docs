---
title: Module oss
title_tag: Module oss | Package pulumi_alicloud | Python SDK
linktitle: oss
notitle: true
---

<div class="section" id="oss">
<h1>oss<a class="headerlink" href="#oss" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.oss"></span><dl class="class">
<dt id="pulumi_alicloud.oss.AwaitableGetBucketObjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">AwaitableGetBucketObjectsResult</code><span class="sig-paren">(</span><em class="sig-param">bucket_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_prefix=None</em>, <em class="sig-param">key_regex=None</em>, <em class="sig-param">objects=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.AwaitableGetBucketObjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.AwaitableGetBucketsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">AwaitableGetBucketsResult</code><span class="sig-paren">(</span><em class="sig-param">buckets=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.AwaitableGetBucketsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.AwaitableGetInstanceAttachmentsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">AwaitableGetInstanceAttachmentsResult</code><span class="sig-paren">(</span><em class="sig-param">attachments=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">vpc_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.AwaitableGetInstanceAttachmentsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.AwaitableGetTablesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">AwaitableGetTablesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.AwaitableGetTablesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.Bucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">Bucket</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cors_rules=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">lifecycle_rules=None</em>, <em class="sig-param">logging=None</em>, <em class="sig-param">logging_isenable=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">referer_config=None</em>, <em class="sig-param">server_side_encryption_rule=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">versioning=None</em>, <em class="sig-param">website=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.Bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a oss bucket and set its attribution.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31898.htm">canned ACL</a> to apply. Can be “private”, “public-read” and “public-read-write”. Defaults to “private”.</p></li>
<li><p><strong>cors_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31903.htm">Cross-Origin Resource Sharing</a> (documented below). The items of core rule are no more than 10 for every OSS bucket.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to “false”.</p></li>
<li><p><strong>lifecycle_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31904.htm">object lifecycle management</a> (documented below).</p></li>
<li><p><strong>logging</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Settings of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31900.htm">bucket logging</a> (documented below).</p></li>
<li><p><strong>logging_isenable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The flag of using logging enable container. Defaults true.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Json format text of bucket policy <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/100680.htm">bucket policy management</a>.</p></li>
<li><p><strong>referer_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31901.htm">referer</a> (documented below).</p></li>
<li><p><strong>server_side_encryption_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of server-side encryption (documented below).</p></li>
<li><p><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.</p></li>
<li><p><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A state of versioning (documented below).</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A website object(documented below).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cors_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which headers are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which origins are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies expose header in the response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies time in seconds that browser can cache the response for a preflight request.</p></li>
</ul>
<p>The <strong>lifecycle_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies lifecycle rule status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a period in the object’s expire (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">date</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like <code class="docutils literal notranslate"><span class="pre">2017-03-09</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Object key prefix identifying one or more objects to which the rule applies.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transitions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">createdBeforeDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>logging</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket that will receive the log objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - To specify a key prefix for log objects.</p></li>
</ul>
<p>The <strong>referer_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Allows referer to be empty. Defaults false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of referer.</p></li>
</ul>
<p>The <strong>server_side_encryption_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sseAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The server-side encryption algorithm to use. Possible values: <code class="docutils literal notranslate"><span class="pre">AES256</span></code> and <code class="docutils literal notranslate"><span class="pre">KMS</span></code>.</p></li>
</ul>
<p>The <strong>versioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the versioning state of a bucket. Valid values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p></li>
</ul>
<p>The <strong>website</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An absolute path to the document to return in case of a 4XX error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31898.htm">canned ACL</a> to apply. Can be “private”, “public-read” and “public-read-write”. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.cors_rules">
<code class="sig-name descname">cors_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.cors_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31903.htm">Cross-Origin Resource Sharing</a> (documented below). The items of core rule are no more than 10 for every OSS bucket.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies which headers are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies which origins are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies expose header in the response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies time in seconds that browser can cache the response for a preflight request.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.extranet_endpoint">
<code class="sig-name descname">extranet_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.extranet_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The extranet access endpoint of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to “false”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.intranet_endpoint">
<code class="sig-name descname">intranet_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.intranet_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The intranet access endpoint of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.lifecycle_rules">
<code class="sig-name descname">lifecycle_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.lifecycle_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31904.htm">object lifecycle management</a> (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies lifecycle rule status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a period in the object’s expire (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">date</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like <code class="docutils literal notranslate"><span class="pre">2017-03-09</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Object key prefix identifying one or more objects to which the rule applies.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transitions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">createdBeforeDate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.logging">
<code class="sig-name descname">logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.logging" title="Permalink to this definition">¶</a></dt>
<dd><p>A Settings of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31900.htm">bucket logging</a> (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the bucket that will receive the log objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - To specify a key prefix for log objects.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.logging_isenable">
<code class="sig-name descname">logging_isenable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.logging_isenable" title="Permalink to this definition">¶</a></dt>
<dd><p>The flag of using logging enable container. Defaults true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Json format text of bucket policy <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/100680.htm">bucket policy management</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.referer_config">
<code class="sig-name descname">referer_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.referer_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31901.htm">referer</a> (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Allows referer to be empty. Defaults false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of referer.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.server_side_encryption_rule">
<code class="sig-name descname">server_side_encryption_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.server_side_encryption_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration of server-side encryption (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sseAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The server-side encryption algorithm to use. Possible values: <code class="docutils literal notranslate"><span class="pre">AES256</span></code> and <code class="docutils literal notranslate"><span class="pre">KMS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.storage_class">
<code class="sig-name descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.versioning">
<code class="sig-name descname">versioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>A state of versioning (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the versioning state of a bucket. Valid values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.Bucket.website">
<code class="sig-name descname">website</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.website" title="Permalink to this definition">¶</a></dt>
<dd><p>A website object(documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An absolute path to the document to return in case of a 4XX error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.oss.Bucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cors_rules=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">extranet_endpoint=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">intranet_endpoint=None</em>, <em class="sig-param">lifecycle_rules=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logging=None</em>, <em class="sig-param">logging_isenable=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">referer_config=None</em>, <em class="sig-param">server_side_encryption_rule=None</em>, <em class="sig-param">storage_class=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">versioning=None</em>, <em class="sig-param">website=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Bucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31898.htm">canned ACL</a> to apply. Can be “private”, “public-read” and “public-read-write”. Defaults to “private”.</p>
</p></li>
<li><p><strong>cors_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A rule of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31903.htm">Cross-Origin Resource Sharing</a> (documented below). The items of core rule are no more than 10 for every OSS bucket.</p>
</p></li>
<li><p><strong>creation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the bucket.</p></li>
<li><p><strong>extranet_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The extranet access endpoint of the bucket.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to “false”.</p></li>
<li><p><strong>intranet_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The intranet access endpoint of the bucket.</p></li>
<li><p><strong>lifecycle_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31904.htm">object lifecycle management</a> (documented below).</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket.</p></li>
<li><p><strong>logging</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A Settings of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31900.htm">bucket logging</a> (documented below).</p>
</p></li>
<li><p><strong>logging_isenable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The flag of using logging enable container. Defaults true.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bucket owner.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Json format text of bucket policy <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/100680.htm">bucket policy management</a>.</p>
</p></li>
<li><p><strong>referer_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The configuration of <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31901.htm">referer</a> (documented below).</p>
</p></li>
<li><p><strong>server_side_encryption_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration of server-side encryption (documented below).</p></li>
<li><p><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.</p></li>
<li><p><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A state of versioning (documented below).</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A website object(documented below).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cors_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which headers are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies which origins are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies expose header in the response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies time in seconds that browser can cache the response for a preflight request.</p></li>
</ul>
<p>The <strong>lifecycle_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies lifecycle rule status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a period in the object’s expire (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">date</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like <code class="docutils literal notranslate"><span class="pre">2017-03-09</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Object key prefix identifying one or more objects to which the rule applies.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transitions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">createdBeforeDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after object creation when the specific rule action takes effect.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: <code class="docutils literal notranslate"><span class="pre">IA</span></code>, <code class="docutils literal notranslate"><span class="pre">Archive</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>logging</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket that will receive the log objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - To specify a key prefix for log objects.</p></li>
</ul>
<p>The <strong>referer_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Allows referer to be empty. Defaults false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of referer.</p></li>
</ul>
<p>The <strong>server_side_encryption_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sseAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The server-side encryption algorithm to use. Possible values: <code class="docutils literal notranslate"><span class="pre">AES256</span></code> and <code class="docutils literal notranslate"><span class="pre">KMS</span></code>.</p></li>
</ul>
<p>The <strong>versioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the versioning state of a bucket. Valid values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p></li>
</ul>
<p>The <strong>website</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An absolute path to the document to return in case of a 4XX error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDocument</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.oss.Bucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oss.Bucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.Bucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oss.BucketObject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">BucketObject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_md5=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to put a object(content or file) to a oss bucket.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52284.htm">canned ACL</a> to apply. Defaults to “private”.</p>
</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the file in.</p></li>
<li><p><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies caching behavior along the request/reply chain. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Cache-Control</a> for further details.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The literal content being uploaded to the bucket.</p></li>
<li><p><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies presentational information for the object. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Disposition</a> for further details.</p></li>
<li><p><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Encoding</a> for further details.</p></li>
<li><p><strong>content_md5</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MD5 value of the content. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31978.htm">MD5</a> for computing method.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p></li>
<li><p><strong>expires</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies expire date for the the request/response. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Expires</a> for further details.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object once it is in the bucket.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the primary key managed by KMS. This parameter is valid when the value of <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span></code> is set to KMS.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies server-side encryption of the object in OSS. Valid values are <code class="docutils literal notranslate"><span class="pre">AES256</span></code>, <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">AES256</span></code>.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the source file being uploaded to the bucket.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52284.htm">canned ACL</a> to apply. Defaults to “private”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put the file in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.cache_control">
<code class="sig-name descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Cache-Control</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The literal content being uploaded to the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content_disposition">
<code class="sig-name descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Disposition</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content_encoding">
<code class="sig-name descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Encoding</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content_length">
<code class="sig-name descname">content_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content_length" title="Permalink to this definition">¶</a></dt>
<dd><p>the content length of request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content_md5">
<code class="sig-name descname">content_md5</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content_md5" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 value of the content. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31978.htm">MD5</a> for computing method.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>the ETag generated for the object (an MD5 sum of the object content).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.expires">
<code class="sig-name descname">expires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.expires" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies expire date for the the request/response. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Expires</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the object once it is in the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the primary key managed by KMS. This parameter is valid when the value of <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span></code> is set to KMS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies server-side encryption of the object in OSS. Valid values are <code class="docutils literal notranslate"><span class="pre">AES256</span></code>, <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">AES256</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the source file being uploaded to the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.BucketObject.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique version ID value for the object, if bucket versioning is enabled.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.oss.BucketObject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">cache_control=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_length=None</em>, <em class="sig-param">content_md5=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">server_side_encryption=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">version_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BucketObject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52284.htm">canned ACL</a> to apply. Defaults to “private”.</p>
</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the file in.</p></li>
<li><p><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies caching behavior along the request/reply chain. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Cache-Control</a> for further details.</p>
</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The literal content being uploaded to the bucket.</p></li>
<li><p><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies presentational information for the object. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Disposition</a> for further details.</p>
</p></li>
<li><p><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Content-Encoding</a> for further details.</p>
</p></li>
<li><p><strong>content_length</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content length of request.</p></li>
<li><p><strong>content_md5</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The MD5 value of the content. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/31978.htm">MD5</a> for computing method.</p>
</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the ETag generated for the object (an MD5 sum of the object content).</p></li>
<li><p><strong>expires</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies expire date for the the request/response. Read <a class="reference external" href="https://www.ietf.org/rfc/rfc2616.txt">RFC2616 Expires</a> for further details.</p>
</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object once it is in the bucket.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the primary key managed by KMS. This parameter is valid when the value of <code class="docutils literal notranslate"><span class="pre">server_side_encryption</span></code> is set to KMS.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies server-side encryption of the object in OSS. Valid values are <code class="docutils literal notranslate"><span class="pre">AES256</span></code>, <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">AES256</span></code>.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the source file being uploaded to the bucket.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique version ID value for the object, if bucket versioning is enabled.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.oss.BucketObject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oss.BucketObject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.BucketObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oss.GetBucketObjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">GetBucketObjectsResult</code><span class="sig-paren">(</span><em class="sig-param">bucket_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_prefix=None</em>, <em class="sig-param">key_regex=None</em>, <em class="sig-param">objects=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketObjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBucketObjects.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetBucketObjectsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketObjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetBucketObjectsResult.objects">
<code class="sig-name descname">objects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketObjectsResult.objects" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of bucket objects. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.GetBucketsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">GetBucketsResult</code><span class="sig-paren">(</span><em class="sig-param">buckets=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBuckets.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetBucketsResult.buckets">
<code class="sig-name descname">buckets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketsResult.buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of buckets. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetBucketsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetBucketsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetBucketsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of bucket names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">GetInstanceAttachmentsResult</code><span class="sig-paren">(</span><em class="sig-param">attachments=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">vpc_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceAttachments.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult.attachments">
<code class="sig-name descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance attachments. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of vpc names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstanceAttachmentsResult.vpc_ids">
<code class="sig-name descname">vpc_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstanceAttachmentsResult.vpc_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of vpc ids.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetInstancesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetInstancesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags of the instance.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.oss.GetTablesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">GetTablesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTables.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetTablesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetTablesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of table IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetTablesResult.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The OTS instance name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetTablesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of table names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.oss.GetTablesResult.tables">
<code class="sig-name descname">tables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oss.GetTablesResult.tables" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tables. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.oss.get_bucket_objects">
<code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">get_bucket_objects</code><span class="sig-paren">(</span><em class="sig-param">bucket_name=None</em>, <em class="sig-param">key_prefix=None</em>, <em class="sig-param">key_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.get_bucket_objects" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the objects of an OSS bucket.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bucket_name</strong> (<em>str</em>) – Name of the bucket that contains the objects to find.</p></li>
<li><p><strong>key_prefix</strong> (<em>str</em>) – Filter results by the given key prefix (such as “path/to/folder/logs-“).</p></li>
<li><p><strong>key_regex</strong> (<em>str</em>) – A regex string to filter results by key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.oss.get_buckets">
<code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">get_buckets</code><span class="sig-paren">(</span><em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.get_buckets" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the OSS buckets of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by bucket name.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.oss.get_instance_attachments">
<code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">get_instance_attachments</code><span class="sig-paren">(</span><em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.get_instance_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the ots instance attachments of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_name</strong> (<em>str</em>) – The name of OTS instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by vpc name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.oss.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the ots instances of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by instance name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the instance. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;oss.getInstances&quot; &quot;instances_ds&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;,
tagKey2 = &quot;tagValue2&quot;
}
}
```
</pre></div>
</div>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.oss.get_tables">
<code class="sig-prename descclassname">pulumi_alicloud.oss.</code><code class="sig-name descname">get_tables</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oss.get_tables" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the ots tables of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.40.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of table IDs.</p></li>
<li><p><strong>instance_name</strong> (<em>str</em>) – The name of OTS instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by table name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
