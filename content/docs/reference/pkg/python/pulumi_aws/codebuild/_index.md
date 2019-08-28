---
title: Module codebuild
---

<div class="section" id="codebuild">
<h1>codebuild<a class="headerlink" href="#codebuild" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codebuild"></span><dl class="class">
<dt id="pulumi_aws.codebuild.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">artifacts=None</em>, <em class="sig-param">badge_enabled=None</em>, <em class="sig-param">build_timeout=None</em>, <em class="sig-param">cache=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encryption_key=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">logs_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secondary_artifacts=None</em>, <em class="sig-param">secondary_sources=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeBuild Project resource. See also the <cite>``codebuild.Webhook`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html">https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html</a>&gt;`_, which manages the webhook to the source (e.g. the “rebuild every time a code change is pushed” option in the CodeBuild web console).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s build output artifacts. Artifact blocks are documented below.</p></li>
<li><p><strong>badge_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Generates a publicly-accessible URL for the projects build badge. Available as <code class="docutils literal notranslate"><span class="pre">badge_url</span></code> attribute when enabled.</p></li>
<li><p><strong>build_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.</p></li>
<li><p><strong>cache</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the cache storage for the project. Cache blocks are documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the project.</p></li>
<li><p><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project’s build output artifacts.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s build environment. Environment blocks are documented below.</p></li>
<li><p><strong>logs_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the builds to store log data to CloudWatch or S3.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><strong>secondary_artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.</p></li>
<li><p><strong>secondary_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s input source code. Source blocks are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_project.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_project.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the CodeBuild project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.artifacts">
<code class="sig-name descname">artifacts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s build output artifacts. Artifact blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.badge_enabled">
<code class="sig-name descname">badge_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.badge_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Generates a publicly-accessible URL for the projects build badge. Available as <code class="docutils literal notranslate"><span class="pre">badge_url</span></code> attribute when enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.badge_url">
<code class="sig-name descname">badge_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.badge_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the build badge when <code class="docutils literal notranslate"><span class="pre">badge_enabled</span></code> is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.build_timeout">
<code class="sig-name descname">build_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.build_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.cache">
<code class="sig-name descname">cache</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the cache storage for the project. Cache blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.encryption_key">
<code class="sig-name descname">encryption_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.encryption_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project’s build output artifacts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.environment">
<code class="sig-name descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s build environment. Environment blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.logs_config">
<code class="sig-name descname">logs_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.logs_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the builds to store log data to CloudWatch or S3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.secondary_artifacts">
<code class="sig-name descname">secondary_artifacts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.secondary_artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.secondary_sources">
<code class="sig-name descname">secondary_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.secondary_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.service_role">
<code class="sig-name descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s input source code. Source blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Project.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">artifacts=None</em>, <em class="sig-param">badge_enabled=None</em>, <em class="sig-param">badge_url=None</em>, <em class="sig-param">build_timeout=None</em>, <em class="sig-param">cache=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encryption_key=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">logs_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secondary_artifacts=None</em>, <em class="sig-param">secondary_sources=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the CodeBuild project.
:param pulumi.Input[dict] artifacts: Information about the project’s build output artifacts. Artifact blocks are documented below.
:param pulumi.Input[bool] badge_enabled: Generates a publicly-accessible URL for the projects build badge. Available as <code class="docutils literal notranslate"><span class="pre">badge_url</span></code> attribute when enabled.
:param pulumi.Input[str] badge_url: The URL of the build badge when <code class="docutils literal notranslate"><span class="pre">badge_enabled</span></code> is enabled.
:param pulumi.Input[float] build_timeout: How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
:param pulumi.Input[dict] cache: Information about the cache storage for the project. Cache blocks are documented below.
:param pulumi.Input[str] description: A short description of the project.
:param pulumi.Input[str] encryption_key: The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project’s build output artifacts.
:param pulumi.Input[dict] environment: Information about the project’s build environment. Environment blocks are documented below.
:param pulumi.Input[dict] logs_config: Configuration for the builds to store log data to CloudWatch or S3.
:param pulumi.Input[str] name: The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object
:param pulumi.Input[list] secondary_artifacts: A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
:param pulumi.Input[list] secondary_sources: A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
:param pulumi.Input[str] service_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
:param pulumi.Input[dict] source: Information about the project’s input source code. Source blocks are documented below.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[dict] vpc_config: Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_project.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_project.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.SourceCredential">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">SourceCredential</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeBuild Source Credentials Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.</p></li>
<li><p><strong>server_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source provider used for this project.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">GitHub</span> <span class="pre">Enterprise</span></code>, this is the personal access token. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>, this is the app password.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Bitbucket username when the authType is <code class="docutils literal notranslate"><span class="pre">BASIC_AUTH</span></code>. This parameter is not valid for other types of source providers or connections.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_source_credential.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_source_credential.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of Source Credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.auth_type">
<code class="sig-name descname">auth_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.auth_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.server_type">
<code class="sig-name descname">server_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The source provider used for this project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.token" title="Permalink to this definition">¶</a></dt>
<dd><p>For <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">GitHub</span> <span class="pre">Enterprise</span></code>, this is the personal access token. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>, this is the app password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Bitbucket username when the authType is <code class="docutils literal notranslate"><span class="pre">BASIC_AUTH</span></code>. This parameter is not valid for other types of source providers or connections.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.SourceCredential.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SourceCredential resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of Source Credential.
:param pulumi.Input[str] auth_type: The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.
:param pulumi.Input[str] server_type: The source provider used for this project.
:param pulumi.Input[str] token: For <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">GitHub</span> <span class="pre">Enterprise</span></code>, this is the personal access token. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>, this is the app password.
:param pulumi.Input[str] user_name: The Bitbucket username when the authType is <code class="docutils literal notranslate"><span class="pre">BASIC_AUTH</span></code>. This parameter is not valid for other types of source providers or connections.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_source_credential.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_source_credential.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.SourceCredential.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.SourceCredential.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Webhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">Webhook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">branch_filter=None</em>, <em class="sig-param">filter_groups=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use <code class="docutils literal notranslate"><span class="pre">filter_group</span></code> over <code class="docutils literal notranslate"><span class="pre">branch_filter</span></code>.</p></li>
<li><p><strong>filter_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the webhook’s trigger. Filter group blocks are documented below.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build project.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.branch_filter">
<code class="sig-name descname">branch_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.branch_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use <code class="docutils literal notranslate"><span class="pre">filter_group</span></code> over <code class="docutils literal notranslate"><span class="pre">branch_filter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.filter_groups">
<code class="sig-name descname">filter_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.filter_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the webhook’s trigger. Filter group blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.payload_url">
<code class="sig-name descname">payload_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.payload_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodeBuild endpoint where webhook events are sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the build project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.secret">
<code class="sig-name descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret token of the associated repository. Not returned by the CodeBuild API for all source types.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codebuild.Webhook.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the webhook.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.Webhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">branch_filter=None</em>, <em class="sig-param">filter_groups=None</em>, <em class="sig-param">payload_url=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Webhook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] branch_filter: A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use <code class="docutils literal notranslate"><span class="pre">filter_group</span></code> over <code class="docutils literal notranslate"><span class="pre">branch_filter</span></code>.
:param pulumi.Input[list] filter_groups: Information about the webhook’s trigger. Filter group blocks are documented below.
:param pulumi.Input[str] payload_url: The CodeBuild endpoint where webhook events are sent.
:param pulumi.Input[str] project_name: The name of the build project.
:param pulumi.Input[str] secret: The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
:param pulumi.Input[str] url: The URL to the webhook.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codebuild.Webhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Webhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
