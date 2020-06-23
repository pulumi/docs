---
title: Module ecr
title_tag: Module ecr | Package pulumi_aws | Python SDK
linktitle: ecr
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "aws" >}}

<div class="section" id="ecr">
<h1>ecr<a class="headerlink" href="#ecr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ecr"></span><dl class="py class">
<dt id="pulumi_aws.ecr.AwaitableGetAuthorizationTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">AwaitableGetAuthorizationTokenResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorization_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetAuthorizationTokenResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.AwaitableGetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">AwaitableGetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorization_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_pushed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_size_in_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.AwaitableGetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">AwaitableGetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">GetAuthorizationTokenResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorization_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthorizationToken.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.authorization_token">
<code class="sig-name descname">authorization_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.authorization_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Temporary IAM authentication credentials to access the ECR repository encoded in base64 in the form of <code class="docutils literal notranslate"><span class="pre">user_name:password</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in UTC RFC3339 format when the authorization token expires.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password decoded from the authorization token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.proxy_endpoint">
<code class="sig-name descname">proxy_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.proxy_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry URL to use in the docker login command.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetAuthorizationTokenResult.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetAuthorizationTokenResult.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User name decoded from the authorization token.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.GetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">GetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorization_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCredentials.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetCredentialsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetCredentialsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_pushed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_size_in_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_pushed_at">
<code class="sig-name descname">image_pushed_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_pushed_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time, expressed as a unix timestamp, at which the current image was pushed to the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_size_in_bytes">
<code class="sig-name descname">image_size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size, in bytes, of the image in the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_tags">
<code class="sig-name descname">image_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of tags associated with this image.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.GetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">GetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepository.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.registry_id">
<code class="sig-name descname">registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.repository_url">
<code class="sig-name descname">repository_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.repository_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ecr.LifecyclePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">LifecyclePolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ECR repository lifecycle policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Only one <code class="docutils literal notranslate"><span class="pre">ecr.LifecyclePolicy</span></code> resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the <code class="docutils literal notranslate"><span class="pre">policy</span></code> JSON.</p>
<p><strong>NOTE:</strong> The AWS ECR API seems to reorder rules based on <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code>. If you define multiple rules that are not sorted in ascending <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code> order in the this provider code, the resource will be flagged for recreation every deployment.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">foopolicy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">LifecyclePolicy</span><span class="p">(</span><span class="s2">&quot;foopolicy&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;rules&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;rulePriority&quot;: 1,</span>
<span class="s2">            &quot;description&quot;: &quot;Expire images older than 14 days&quot;,</span>
<span class="s2">            &quot;selection&quot;: {</span>
<span class="s2">                &quot;tagStatus&quot;: &quot;untagged&quot;,</span>
<span class="s2">                &quot;countType&quot;: &quot;sinceImagePushed&quot;,</span>
<span class="s2">                &quot;countUnit&quot;: &quot;days&quot;,</span>
<span class="s2">                &quot;countNumber&quot;: 14</span>
<span class="s2">            },</span>
<span class="s2">            &quot;action&quot;: {</span>
<span class="s2">                &quot;type&quot;: &quot;expire&quot;</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">foopolicy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">LifecyclePolicy</span><span class="p">(</span><span class="s2">&quot;foopolicy&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;rules&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;rulePriority&quot;: 1,</span>
<span class="s2">            &quot;description&quot;: &quot;Keep last 30 images&quot;,</span>
<span class="s2">            &quot;selection&quot;: {</span>
<span class="s2">                &quot;tagStatus&quot;: &quot;tagged&quot;,</span>
<span class="s2">                &quot;tagPrefixList&quot;: [&quot;v&quot;],</span>
<span class="s2">                &quot;countType&quot;: &quot;imageCountMoreThan&quot;,</span>
<span class="s2">                &quot;countNumber&quot;: 30</span>
<span class="s2">            },</span>
<span class="s2">            &quot;action&quot;: {</span>
<span class="s2">                &quot;type&quot;: &quot;expire&quot;</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.registry_id">
<code class="sig-name descname">registry_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository to apply the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.LifecyclePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecyclePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.</p>
</p></li>
<li><p><strong>registry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registry ID where the repository was created.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.LifecyclePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.LifecyclePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.Repository">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">Repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_scanning_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tag_mutability</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">image_scanning_configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;scanOnPush&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">image_tag_mutability</span><span class="o">=</span><span class="s2">&quot;MUTABLE&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>image_scanning_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html">ECR User Guide</a> for more information about image scanning.</p></li>
<li><p><strong>image_tag_mutability</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>image_scanning_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scanOnPush</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.image_scanning_configuration">
<code class="sig-name descname">image_scanning_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.image_scanning_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html">ECR User Guide</a> for more information about image scanning.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scanOnPush</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.image_tag_mutability">
<code class="sig-name descname">image_tag_mutability</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.image_tag_mutability" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.registry_id">
<code class="sig-name descname">registry_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.repository_url">
<code class="sig-name descname">repository_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.repository_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.Repository.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.Repository.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_scanning_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tag_mutability</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Repository resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full ARN of the repository.</p></li>
<li><p><strong>image_scanning_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the <a class="reference external" href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html">ECR User Guide</a> for more information about image scanning.</p>
</p></li>
<li><p><strong>image_tag_mutability</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</p></li>
<li><p><strong>registry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registry ID where the repository was created.</p></li>
<li><p><strong>repository_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>image_scanning_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scanOnPush</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.Repository.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.Repository.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.RepositoryPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">RepositoryPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository Policy.</p>
<p>Note that currently only one policy may be applied to a repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">foopolicy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">RepositoryPolicy</span><span class="p">(</span><span class="s2">&quot;foopolicy&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2008-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Sid&quot;: &quot;new policy&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: &quot;*&quot;,</span>
<span class="s2">            &quot;Action&quot;: [</span>
<span class="s2">                &quot;ecr:GetDownloadUrlForLayer&quot;,</span>
<span class="s2">                &quot;ecr:BatchGetImage&quot;,</span>
<span class="s2">                &quot;ecr:BatchCheckLayerAvailability&quot;,</span>
<span class="s2">                &quot;ecr:PutImage&quot;,</span>
<span class="s2">                &quot;ecr:InitiateLayerUpload&quot;,</span>
<span class="s2">                &quot;ecr:UploadLayerPart&quot;,</span>
<span class="s2">                &quot;ecr:CompleteLayerUpload&quot;,</span>
<span class="s2">                &quot;ecr:DescribeRepositories&quot;,</span>
<span class="s2">                &quot;ecr:GetRepositoryPolicy&quot;,</span>
<span class="s2">                &quot;ecr:ListImages&quot;,</span>
<span class="s2">                &quot;ecr:DeleteRepository&quot;,</span>
<span class="s2">                &quot;ecr:BatchDeleteImage&quot;,</span>
<span class="s2">                &quot;ecr:SetRepositoryPolicy&quot;,</span>
<span class="s2">                &quot;ecr:DeleteRepositoryPolicy&quot;</span>
<span class="s2">            ]</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The policy document. This is a JSON formatted string.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.registry_id">
<code class="sig-name descname">registry_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository to apply the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.RepositoryPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The policy document. This is a JSON formatted string.</p></li>
<li><p><strong>registry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registry ID where the repository was created.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ecr.RepositoryPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.RepositoryPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.get_authorization_token">
<code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">get_authorization_token</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_authorization_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Authorization Token data source allows the authorization token, proxy endpoint, token expiration date, user name and password to be retrieved for an ECR repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">token</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">get_authorization_token</span><span class="p">()</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>registry_id</strong> (<em>str</em>) – AWS account ID of the ECR Repository. If not specified the default account is assumed.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ecr.get_credentials">
<code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">get_credentials</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ecr.get_image">
<code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">image_digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Image data source allows the details of an image with a particular tag or digest to be retrieved.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">service_image</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">get_image</span><span class="p">(</span><span class="n">image_tag</span><span class="o">=</span><span class="s2">&quot;latest&quot;</span><span class="p">,</span>
    <span class="n">repository_name</span><span class="o">=</span><span class="s2">&quot;my/service&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image_digest</strong> (<em>str</em>) – The sha256 digest of the image manifest. At least one of <code class="docutils literal notranslate"><span class="pre">image_digest</span></code> or <code class="docutils literal notranslate"><span class="pre">image_tag</span></code> must be specified.</p></li>
<li><p><strong>image_tag</strong> (<em>str</em>) – The tag associated with this image. At least one of <code class="docutils literal notranslate"><span class="pre">image_digest</span></code> or <code class="docutils literal notranslate"><span class="pre">image_tag</span></code> must be specified.</p></li>
<li><p><strong>registry_id</strong> (<em>str</em>) – The ID of the Registry where the repository resides.</p></li>
<li><p><strong>repository_name</strong> (<em>str</em>) – The name of the ECR Repository.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ecr.get_repository">
<code class="sig-prename descclassname">pulumi_aws.ecr.</code><code class="sig-name descname">get_repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Repository data source allows the ARN, Repository URI and Registry ID to be retrieved for an ECR repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">service</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ecr</span><span class="o">.</span><span class="n">get_repository</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;ecr-repository&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the ECR Repository.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
