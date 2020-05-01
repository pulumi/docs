---
title: Module cloudfront
title_tag: Module cloudfront | Package pulumi_aws | Python SDK
linktitle: cloudfront
notitle: true
---

<div class="section" id="cloudfront">
<h1>cloudfront<a class="headerlink" href="#cloudfront" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudfront"></span><dl class="py class">
<dt id="pulumi_aws.cloudfront.AwaitableGetDistributionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">AwaitableGetDistributionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosted_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_progress_validation_batches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.AwaitableGetDistributionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudfront.Distribution">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">Distribution</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_error_responses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_cache_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_root_object</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_ipv6_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ordered_cache_behaviors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrictions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retain_on_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viewer_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_deployment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_acl_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront web distribution.</p>
<p>For information about CloudFront distributions, see the
<a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html">Amazon CloudFront Developer Guide</a>. For specific information about creating
CloudFront web distributions, see the <a class="reference external" href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html">POST Distribution</a> page in the Amazon
CloudFront API Reference.</p>
<blockquote>
<div><p><strong>NOTE:</strong> CloudFront distributions take about 15 minutes to a deployed state
after creation or modification. During this time, deletes to resources will be
blocked. If you need to delete a distribution that is enabled and you do not
want to wait, you need to use the <code class="docutils literal notranslate"><span class="pre">retain_on_delete</span></code> flag.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Extra CNAMEs (alternate domain names), if any, for
this distribution.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any comments you want to include about the
distribution.</p></li>
<li><p><strong>custom_error_responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more custom error response elements (multiples allowed).</p></li>
<li><p><strong>default_cache_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default cache behavior for this distribution (maximum
one).</p></li>
<li><p><strong>default_root_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the distribution is enabled to accept end
user requests for content.</p></li>
<li><p><strong>http_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p></li>
<li><p><strong>is_ipv6_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the IPv6 is enabled for the distribution.</p></li>
<li><p><strong>logging_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The logging
configuration that controls how logs are written
to your distribution (maximum one).</p></li>
<li><p><strong>ordered_cache_behaviors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p></li>
<li><p><strong>origin_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origin_group for this
distribution (multiples allowed).</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origins for this
distribution (multiples allowed).</p></li>
<li><p><strong>price_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The restriction
configuration for this distribution (maximum one).</p></li>
<li><p><strong>retain_on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>viewer_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SSL
configuration for this distribution (maximum
one).</p></li>
<li><p><strong>wait_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_error_responses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorCachingMinTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The 4xx or 5xx HTTP status code that you want to
customize.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responsePagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the custom error page (for
example, <code class="docutils literal notranslate"><span class="pre">/custom_404.html</span></code>).</p></li>
</ul>
<p>The <strong>default_cache_behavior</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
<p>The <strong>logging_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket to store the access logs in, for
example, <code class="docutils literal notranslate"><span class="pre">myawslogbucket.s3.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeCookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether you want CloudFront to
include cookies in access logs (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, <code class="docutils literal notranslate"><span class="pre">myprefix/</span></code>.</p></li>
</ul>
<p>The <strong>ordered_cache_behaviors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The pattern (for example, <code class="docutils literal notranslate"><span class="pre">images/*.jpg)</span></code> that
specifies which requests you want this cache behavior to apply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
<p>The <strong>origin_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverCriteria</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The failover criteria for when to failover to the secondary origin</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of HTTP status codes for the origin group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
</ul>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more sub-resources with <code class="docutils literal notranslate"><span class="pre">name</span></code> and
<code class="docutils literal notranslate"><span class="pre">value</span></code> parameters that specify header data that will be sent to the origin
(multiples allowed).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customOriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudFront custom
origin configuration information. If an S3
origin is required, use <code class="docutils literal notranslate"><span class="pre">s3_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originKeepaliveTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The origin protocol policy to apply to
your origin. One of <code class="docutils literal notranslate"><span class="pre">http-only</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">match-viewer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Custom Read timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originSslProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">TLSv1.2</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3OriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudFront S3 origin
configuration information. If a custom origin is required, use
<code class="docutils literal notranslate"><span class="pre">custom_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originAccessIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The [CloudFront origin access
identity][5] to associate with the origin.</p></li>
</ul>
</li>
</ul>
<p>The <strong>restrictions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">geoRestriction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (<code class="docutils literal notranslate"><span class="pre">whitelist</span></code>) or not
distribute your content (<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method that you want to use to restrict
distribution of your content by country: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, or
<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>viewer_certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acmCertificateArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the <a class="reference external" href="https://aws.amazon.com/certificate-manager/">AWS Certificate Manager</a>
certificate that you wish to use with this distribution. Specify this,
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.  The ACM
certificate must be in  US-EAST-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudfrontDefaultCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want viewers to use HTTPS
to request your objects and you’re using the CloudFront domain name for your
distribution. Specify this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iamCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span> <span class="pre">=</span> <span class="pre">false</span></code>. One of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>,
<code class="docutils literal notranslate"><span class="pre">TLSv1_2016</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1_2016</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1.2_2018</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>. <strong>NOTE</strong>:
If you are using a custom certificate (specified with <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>
or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>), and have specified <code class="docutils literal notranslate"><span class="pre">sni-only</span></code> in
<code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> or later must be specified. If you have
specified <code class="docutils literal notranslate"><span class="pre">vip</span></code> in <code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, only <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> can be
specified. If you have specified <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>
must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSupportMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.active_trusted_signers">
<code class="sig-name descname">active_trusted_signers</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.active_trusted_signers" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.aliases">
<code class="sig-name descname">aliases</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra CNAMEs (alternate domain names), if any, for
this distribution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the distribution configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.comment">
<code class="sig-name descname">comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Any comments you want to include about the
distribution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.custom_error_responses">
<code class="sig-name descname">custom_error_responses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.custom_error_responses" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more custom error response elements (multiples allowed).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorCachingMinTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The 4xx or 5xx HTTP status code that you want to
customize.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responsePagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of the custom error page (for
example, <code class="docutils literal notranslate"><span class="pre">/custom_404.html</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_cache_behavior">
<code class="sig-name descname">default_cache_behavior</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_cache_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The default cache behavior for this distribution (maximum
one).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_root_object">
<code class="sig-name descname">default_root_object</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_root_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the distribution is enabled to accept end
user requests for content.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFront Route 53 zone ID that can be used to
route an <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html">Alias Resource Record Set</a> to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.http_version">
<code class="sig-name descname">http_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.http_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.in_progress_validation_batches">
<code class="sig-name descname">in_progress_validation_batches</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.in_progress_validation_batches" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of invalidation batches
currently in progress.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.is_ipv6_enabled">
<code class="sig-name descname">is_ipv6_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.is_ipv6_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the IPv6 is enabled for the distribution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the distribution was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.logging_config">
<code class="sig-name descname">logging_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.logging_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging
configuration that controls how logs are written
to your distribution (maximum one).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 bucket to store the access logs in, for
example, <code class="docutils literal notranslate"><span class="pre">myawslogbucket.s3.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeCookies</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether you want CloudFront to
include cookies in access logs (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, <code class="docutils literal notranslate"><span class="pre">myprefix/</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors">
<code class="sig-name descname">ordered_cache_behaviors</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors" title="Permalink to this definition">¶</a></dt>
<dd><p>An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The pattern (for example, <code class="docutils literal notranslate"><span class="pre">images/*.jpg)</span></code> that
specifies which requests you want this cache behavior to apply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origin_groups">
<code class="sig-name descname">origin_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origin_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origin_group for this
distribution (multiples allowed).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverCriteria</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The failover criteria for when to failover to the secondary origin</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of HTTP status codes for the origin group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the member origin</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the member origin</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origins">
<code class="sig-name descname">origins</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origins for this
distribution (multiples allowed).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more sub-resources with <code class="docutils literal notranslate"><span class="pre">name</span></code> and
<code class="docutils literal notranslate"><span class="pre">value</span></code> parameters that specify header data that will be sent to the origin
(multiples allowed).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customOriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudFront custom
origin configuration information. If an S3
origin is required, use <code class="docutils literal notranslate"><span class="pre">s3_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTPS port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originKeepaliveTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The origin protocol policy to apply to
your origin. One of <code class="docutils literal notranslate"><span class="pre">http-only</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">match-viewer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Custom Read timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originSslProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">TLSv1.2</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the member origin</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3OriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudFront S3 origin
configuration information. If a custom origin is required, use
<code class="docutils literal notranslate"><span class="pre">custom_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originAccessIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The [CloudFront origin access
identity][5] to associate with the origin.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.price_class">
<code class="sig-name descname">price_class</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.price_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.restrictions">
<code class="sig-name descname">restrictions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.restrictions" title="Permalink to this definition">¶</a></dt>
<dd><p>The restriction
configuration for this distribution (maximum one).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">geoRestriction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (<code class="docutils literal notranslate"><span class="pre">whitelist</span></code>) or not
distribute your content (<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The method that you want to use to restrict
distribution of your content by country: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, or
<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.retain_on_delete">
<code class="sig-name descname">retain_on_delete</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.retain_on_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.viewer_certificate">
<code class="sig-name descname">viewer_certificate</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.viewer_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL
configuration for this distribution (maximum
one).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acmCertificateArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the <a class="reference external" href="https://aws.amazon.com/certificate-manager/">AWS Certificate Manager</a>
certificate that you wish to use with this distribution. Specify this,
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.  The ACM
certificate must be in  US-EAST-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudfrontDefaultCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want viewers to use HTTPS
to request your objects and you’re using the CloudFront domain name for your
distribution. Specify this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iamCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span> <span class="pre">=</span> <span class="pre">false</span></code>. One of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>,
<code class="docutils literal notranslate"><span class="pre">TLSv1_2016</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1_2016</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1.2_2018</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>. <strong>NOTE</strong>:
If you are using a custom certificate (specified with <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>
or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>), and have specified <code class="docutils literal notranslate"><span class="pre">sni-only</span></code> in
<code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> or later must be specified. If you have
specified <code class="docutils literal notranslate"><span class="pre">vip</span></code> in <code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, only <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> can be
specified. If you have specified <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>
must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSupportMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.wait_for_deployment">
<code class="sig-name descname">wait_for_deployment</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.wait_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.Distribution.web_acl_id">
<code class="sig-name descname">web_acl_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.web_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.Distribution.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_trusted_signers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">caller_reference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_error_responses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_cache_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_root_object</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosted_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_progress_validation_batches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_ipv6_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ordered_cache_behaviors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrictions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retain_on_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viewer_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_deployment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_acl_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Distribution resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_trusted_signers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.</p></li>
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Extra CNAMEs (alternate domain names), if any, for
this distribution.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p></li>
<li><p><strong>caller_reference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal value used by CloudFront to allow future
updates to the distribution configuration.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any comments you want to include about the
distribution.</p></li>
<li><p><strong>custom_error_responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more custom error response elements (multiples allowed).</p></li>
<li><p><strong>default_cache_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default cache behavior for this distribution (maximum
one).</p></li>
<li><p><strong>default_root_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the distribution is enabled to accept end
user requests for content.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The CloudFront Route 53 zone ID that can be used to
route an <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html">Alias Resource Record Set</a> to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p>
</p></li>
<li><p><strong>http_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p></li>
<li><p><strong>in_progress_validation_batches</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of invalidation batches
currently in progress.</p></li>
<li><p><strong>is_ipv6_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the IPv6 is enabled for the distribution.</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time the distribution was last modified.</p></li>
<li><p><strong>logging_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The logging
configuration that controls how logs are written
to your distribution (maximum one).</p></li>
<li><p><strong>ordered_cache_behaviors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p></li>
<li><p><strong>origin_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origin_group for this
distribution (multiples allowed).</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origins for this
distribution (multiples allowed).</p></li>
<li><p><strong>price_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The restriction
configuration for this distribution (maximum one).</p></li>
<li><p><strong>retain_on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>viewer_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SSL
configuration for this distribution (maximum
one).</p></li>
<li><p><strong>wait_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_error_responses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">errorCachingMinTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The 4xx or 5xx HTTP status code that you want to
customize.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responsePagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the custom error page (for
example, <code class="docutils literal notranslate"><span class="pre">/custom_404.html</span></code>).</p></li>
</ul>
<p>The <strong>default_cache_behavior</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
<p>The <strong>logging_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket to store the access logs in, for
example, <code class="docutils literal notranslate"><span class="pre">myawslogbucket.s3.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeCookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether you want CloudFront to
include cookies in access logs (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, <code class="docutils literal notranslate"><span class="pre">myprefix/</span></code>.</p></li>
</ul>
<p>The <strong>ordered_cache_behaviors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls whether CloudFront caches the
response to requests using the specified HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you want CloudFront to automatically
compress content for web requests that include <code class="docutils literal notranslate"><span class="pre">Accept-Encoding:</span> <span class="pre">gzip</span></code> in
the request header (default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code> or <code class="docutils literal notranslate"><span class="pre">Expires</span></code> header. Defaults to
1 day.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLevelEncryptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field level encryption configuration ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cookies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>. If <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, you must include the
subsequent <code class="docutils literal notranslate"><span class="pre">whitelisted_names</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">whitelistedNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If you have specified <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> to
<code class="docutils literal notranslate"><span class="pre">forward</span></code>, the whitelisted cookies that you want CloudFront to forward to
your origin.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to include all
headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringCacheKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - When specified, along with a value of
<code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">query_string</span></code>, all query string keys are cached.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaFunctionAssociations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific event to trigger this function.
Valid values: <code class="docutils literal notranslate"><span class="pre">viewer-request</span></code>, <code class="docutils literal notranslate"><span class="pre">origin-request</span></code>, <code class="docutils literal notranslate"><span class="pre">viewer-response</span></code>,
<code class="docutils literal notranslate"><span class="pre">origin-response</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of <code class="docutils literal notranslate"><span class="pre">Cache-Control</span> <span class="pre">max-age</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span>
<span class="pre">s-maxage</span></code>, and <code class="docutils literal notranslate"><span class="pre">Expires</span></code> headers. Defaults to 365 days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The pattern (for example, <code class="docutils literal notranslate"><span class="pre">images/*.jpg)</span></code> that
specifies which requests you want this cache behavior to apply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smoothStreaming</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetOriginId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedSigners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The AWS accounts, if any, that you want to
allow to create signed URLs for private content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewerProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of <code class="docutils literal notranslate"><span class="pre">allow-all</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">redirect-to-https</span></code>.</p></li>
</ul>
<p>The <strong>origin_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverCriteria</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The failover criteria for when to failover to the secondary origin</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of HTTP status codes for the origin group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
</ul>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more sub-resources with <code class="docutils literal notranslate"><span class="pre">name</span></code> and
<code class="docutils literal notranslate"><span class="pre">value</span></code> parameters that specify header data that will be sent to the origin
(multiples allowed).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customOriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudFront custom
origin configuration information. If an S3
origin is required, use <code class="docutils literal notranslate"><span class="pre">s3_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS port the custom origin listens on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originKeepaliveTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originProtocolPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The origin protocol policy to apply to
your origin. One of <code class="docutils literal notranslate"><span class="pre">http-only</span></code>, <code class="docutils literal notranslate"><span class="pre">https-only</span></code>, or <code class="docutils literal notranslate"><span class="pre">match-viewer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Custom Read timeout, in seconds. By default, AWS enforces a limit of <code class="docutils literal notranslate"><span class="pre">60</span></code>. But you can request an <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout">increase</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originSslProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">TLSv1.2</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the member origin</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3OriginConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudFront S3 origin
configuration information. If a custom origin is required, use
<code class="docutils literal notranslate"><span class="pre">custom_origin_config</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originAccessIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The [CloudFront origin access
identity][5] to associate with the origin.</p></li>
</ul>
</li>
</ul>
<p>The <strong>restrictions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">geoRestriction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (<code class="docutils literal notranslate"><span class="pre">whitelist</span></code>) or not
distribute your content (<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method that you want to use to restrict
distribution of your content by country: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">whitelist</span></code>, or
<code class="docutils literal notranslate"><span class="pre">blacklist</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>viewer_certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acmCertificateArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the <a class="reference external" href="https://aws.amazon.com/certificate-manager/">AWS Certificate Manager</a>
certificate that you wish to use with this distribution. Specify this,
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.  The ACM
certificate must be in  US-EAST-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudfrontDefaultCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want viewers to use HTTPS
to request your objects and you’re using the CloudFront domain name for your
distribution. Specify this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iamCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>, or <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
<code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span> <span class="pre">=</span> <span class="pre">false</span></code>. One of <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>,
<code class="docutils literal notranslate"><span class="pre">TLSv1_2016</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1.1_2016</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1.2_2018</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>. <strong>NOTE</strong>:
If you are using a custom certificate (specified with <code class="docutils literal notranslate"><span class="pre">acm_certificate_arn</span></code>
or <code class="docutils literal notranslate"><span class="pre">iam_certificate_id</span></code>), and have specified <code class="docutils literal notranslate"><span class="pre">sni-only</span></code> in
<code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> or later must be specified. If you have
specified <code class="docutils literal notranslate"><span class="pre">vip</span></code> in <code class="docutils literal notranslate"><span class="pre">ssl_support_method</span></code>, only <code class="docutils literal notranslate"><span class="pre">SSLv3</span></code> or <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code> can be
specified. If you have specified <code class="docutils literal notranslate"><span class="pre">cloudfront_default_certificate</span></code>, <code class="docutils literal notranslate"><span class="pre">TLSv1</span></code>
must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSupportMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.Distribution.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.Distribution.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.GetDistributionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">GetDistributionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosted_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_progress_validation_batches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDistribution.</p>
<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name corresponding to the distribution. For
example: <code class="docutils literal notranslate"><span class="pre">d604721fxaaqy9.cloudfront.net</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier for the distribution. For example: <code class="docutils literal notranslate"><span class="pre">EDFDVBD632BHDS5</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.in_progress_validation_batches">
<code class="sig-name descname">in_progress_validation_batches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.in_progress_validation_batches" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of invalidation batches
currently in progress.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the distribution was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.GetDistributionResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.GetDistributionResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">OriginAccessIdentity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront origin access identity.</p>
<p>For information about CloudFront distributions, see the
<a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html">Amazon CloudFront Developer Guide</a>. For more information on generating
origin access identities, see
[Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment for the origin access identity.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the origin access identity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path">
<code class="sig-name descname">cloudfront_access_identity_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A shortcut to the full path for the
origin access identity to use in CloudFront, see below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.comment">
<code class="sig-name descname">comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment for the origin access identity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the origin access identity’s information.
For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn">
<code class="sig-name descname">iam_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A pre-generated ARN for use in S3 bucket policies (see below).
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::cloudfront:user/CloudFront</span> <span class="pre">Origin</span> <span class="pre">Access</span> <span class="pre">Identity</span>
<span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id">
<code class="sig-name descname">s3_canonical_user_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 canonical user ID for the origin
access identity, which you use when giving the origin access identity read
permission to an object in Amazon S3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">caller_reference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloudfront_access_identity_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_canonical_user_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OriginAccessIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>caller_reference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal value used by CloudFront to allow future
updates to the origin access identity.</p></li>
<li><p><strong>cloudfront_access_identity_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shortcut to the full path for the
origin access identity to use in CloudFront, see below.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment for the origin access identity.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the origin access identity’s information.
For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>iam_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A pre-generated ARN for use in S3 bucket policies (see below).
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::cloudfront:user/CloudFront</span> <span class="pre">Origin</span> <span class="pre">Access</span> <span class="pre">Identity</span>
<span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>s3_canonical_user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 canonical user ID for the origin
access identity, which you use when giving the origin access identity read
permission to an object in Amazon S3.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">PublicKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encoded_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the public key.</p></li>
<li><p><strong>encoded_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future updates to the public key configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.comment">
<code class="sig-name descname">comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the public key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.encoded_key">
<code class="sig-name descname">encoded_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.encoded_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the public key. For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the public key. By default generated by this provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.PublicKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">caller_reference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encoded_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>caller_reference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal value used by CloudFront to allow future updates to the public key configuration.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the public key.</p></li>
<li><p><strong>encoded_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the public key. For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudfront.PublicKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.cloudfront.get_distribution">
<code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">get_distribution</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.get_distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a CloudFront distribution.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The identifier for the distribution. For example: <code class="docutils literal notranslate"><span class="pre">EDFDVBD632BHDS5</span></code>.</p>
</dd>
</dl>
</dd></dl>

</div>
