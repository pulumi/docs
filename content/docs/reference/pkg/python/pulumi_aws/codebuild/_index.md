---
title: Module codebuild
title_tag: Module codebuild | Package pulumi_aws | Python SDK
linktitle: codebuild
notitle: true
---

<div class="section" id="codebuild">
<h1>codebuild<a class="headerlink" href="#codebuild" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codebuild"></span><dl class="py class">
<dt id="pulumi_aws.codebuild.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">artifacts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">badge_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">build_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queued_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_artifacts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The projects name.</p></li>
<li><p><strong>queued_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.</p></li>
<li><p><strong>secondary_artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.</p></li>
<li><p><strong>secondary_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s input source code. Source blocks are documented below.</p></li>
<li><p><strong>source_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version of the build input to be built for this project. If not specified, the latest version is used.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>artifacts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>cache</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location where the AWS CodeBuild project stores cached resources. For type <code class="docutils literal notranslate"><span class="pre">S3</span></code> the value must be a valid S3 bucket name/prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  <code class="docutils literal notranslate"><span class="pre">LOCAL_SOURCE_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL_DOCKER_LAYER_CACHE</span></code>, and <code class="docutils literal notranslate"><span class="pre">LOCAL_CUSTOM_CACHE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of storage that will be used for the AWS CodeBuild project cache. Valid values: <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL</span></code>, and <code class="docutils literal notranslate"><span class="pre">S3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>.</p></li>
</ul>
<p>The <strong>environment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the compute resources the build project will use. Available values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code> or <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_2XLARGE</span></code>. <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code> is only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">compute_type</span></code> need to be <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of environment variables to make available to builds for this build project.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The environment variable’s name or key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of environment variable. Valid values: <code class="docutils literal notranslate"><span class="pre">PARAMETER_STORE</span></code>, <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The environment variable’s value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Docker image to use for this build project. Valid values include <a class="reference external" href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html">Docker images provided by CodeBuild</a> (e.g <code class="docutils literal notranslate"><span class="pre">aws/codebuild/standard:2.0</span></code>), <a class="reference external" href="https://hub.docker.com/">Docker Hub images</a> (e.g. <code class="docutils literal notranslate"><span class="pre">nginx:latest</span></code>), and full Docker repository URIs such as those for ECR (e.g. <code class="docutils literal notranslate"><span class="pre">137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imagePullCredentialsType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code> or <code class="docutils literal notranslate"><span class="pre">SERVICE_ROLE</span></code>. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privilegedMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, enables running the Docker daemon inside a Docker container. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryCredential</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credential</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build environment to use for related builds. Available values are: <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">WINDOWS_CONTAINER</span></code> or <code class="docutils literal notranslate"><span class="pre">ARM_CONTAINER</span></code>.</p></li>
</ul>
<p>The <strong>logs_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for the builds to store logs to CloudWatch</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name of the logs in CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Current status of logs in S3 for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The stream name of the logs in CloudWatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Logs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for the builds to store logs to S3.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Current status of logs in CloudWatch Logs for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>secondary_artifacts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket. If <code class="docutils literal notranslate"><span class="pre">path</span></code> is not also specified, then <code class="docutils literal notranslate"><span class="pre">location</span></code> can also specify the path of the output artifact in the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>secondary_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build spec declaration to use for this build project’s related builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when your source provider is <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, or <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build spec declaration to use for this build project’s related builds. This must be set when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security group IDs to assign to running builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The subnet IDs within which to run builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the VPC within which to run builds.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the CodeBuild project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.artifacts">
<code class="sig-name descname">artifacts</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s build output artifacts. Artifact blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.badge_enabled">
<code class="sig-name descname">badge_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.badge_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Generates a publicly-accessible URL for the projects build badge. Available as <code class="docutils literal notranslate"><span class="pre">badge_url</span></code> attribute when enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.badge_url">
<code class="sig-name descname">badge_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.badge_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the build badge when <code class="docutils literal notranslate"><span class="pre">badge_enabled</span></code> is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.build_timeout">
<code class="sig-name descname">build_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.build_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.cache">
<code class="sig-name descname">cache</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the cache storage for the project. Cache blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location where the AWS CodeBuild project stores cached resources. For type <code class="docutils literal notranslate"><span class="pre">S3</span></code> the value must be a valid S3 bucket name/prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  <code class="docutils literal notranslate"><span class="pre">LOCAL_SOURCE_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL_DOCKER_LAYER_CACHE</span></code>, and <code class="docutils literal notranslate"><span class="pre">LOCAL_CUSTOM_CACHE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of storage that will be used for the AWS CodeBuild project cache. Valid values: <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL</span></code>, and <code class="docutils literal notranslate"><span class="pre">S3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.encryption_key">
<code class="sig-name descname">encryption_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.encryption_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project’s build output artifacts.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.environment">
<code class="sig-name descname">environment</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s build environment. Environment blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information about the compute resources the build project will use. Available values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code> or <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_2XLARGE</span></code>. <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code> is only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">compute_type</span></code> need to be <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of environment variables to make available to builds for this build project.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The environment variable’s name or key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of environment variable. Valid values: <code class="docutils literal notranslate"><span class="pre">PARAMETER_STORE</span></code>, <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The environment variable’s value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Docker image to use for this build project. Valid values include <a class="reference external" href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html">Docker images provided by CodeBuild</a> (e.g <code class="docutils literal notranslate"><span class="pre">aws/codebuild/standard:2.0</span></code>), <a class="reference external" href="https://hub.docker.com/">Docker Hub images</a> (e.g. <code class="docutils literal notranslate"><span class="pre">nginx:latest</span></code>), and full Docker repository URIs such as those for ECR (e.g. <code class="docutils literal notranslate"><span class="pre">137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imagePullCredentialsType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code> or <code class="docutils literal notranslate"><span class="pre">SERVICE_ROLE</span></code>. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privilegedMode</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, enables running the Docker daemon inside a Docker container. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryCredential</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credential</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of build environment to use for related builds. Available values are: <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">WINDOWS_CONTAINER</span></code> or <code class="docutils literal notranslate"><span class="pre">ARM_CONTAINER</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.logs_config">
<code class="sig-name descname">logs_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.logs_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the builds to store log data to CloudWatch or S3.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration for the builds to store logs to CloudWatch</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The group name of the logs in CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Current status of logs in S3 for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The stream name of the logs in CloudWatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Logs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration for the builds to store logs to S3.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Current status of logs in CloudWatch Logs for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The projects name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.queued_timeout">
<code class="sig-name descname">queued_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.queued_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.secondary_artifacts">
<code class="sig-name descname">secondary_artifacts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.secondary_artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket. If <code class="docutils literal notranslate"><span class="pre">path</span></code> is not also specified, then <code class="docutils literal notranslate"><span class="pre">location</span></code> can also specify the path of the output artifact in the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.secondary_sources">
<code class="sig-name descname">secondary_sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.secondary_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The build spec declaration to use for this build project’s related builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when your source provider is <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, or <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.service_role">
<code class="sig-name descname">service_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.source">
<code class="sig-name descname">source</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the project’s input source code. Source blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The build spec declaration to use for this build project’s related builds. This must be set when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.source_version">
<code class="sig-name descname">source_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.source_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A version of the build input to be built for this project. If not specified, the latest version is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Project.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Project.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The security group IDs to assign to running builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The subnet IDs within which to run builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the VPC within which to run builds.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">artifacts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">badge_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">badge_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">build_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queued_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_artifacts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the CodeBuild project.</p></li>
<li><p><strong>artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s build output artifacts. Artifact blocks are documented below.</p></li>
<li><p><strong>badge_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Generates a publicly-accessible URL for the projects build badge. Available as <code class="docutils literal notranslate"><span class="pre">badge_url</span></code> attribute when enabled.</p></li>
<li><p><strong>badge_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the build badge when <code class="docutils literal notranslate"><span class="pre">badge_enabled</span></code> is enabled.</p></li>
<li><p><strong>build_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.</p></li>
<li><p><strong>cache</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the cache storage for the project. Cache blocks are documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the project.</p></li>
<li><p><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project’s build output artifacts.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s build environment. Environment blocks are documented below.</p></li>
<li><p><strong>logs_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the builds to store log data to CloudWatch or S3.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The projects name.</p></li>
<li><p><strong>queued_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.</p></li>
<li><p><strong>secondary_artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.</p></li>
<li><p><strong>secondary_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the project’s input source code. Source blocks are documented below.</p></li>
<li><p><strong>source_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version of the build input to be built for this project. If not specified, the latest version is used.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the builds to run inside a VPC. VPC config blocks are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>artifacts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>cache</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location where the AWS CodeBuild project stores cached resources. For type <code class="docutils literal notranslate"><span class="pre">S3</span></code> the value must be a valid S3 bucket name/prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  <code class="docutils literal notranslate"><span class="pre">LOCAL_SOURCE_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL_DOCKER_LAYER_CACHE</span></code>, and <code class="docutils literal notranslate"><span class="pre">LOCAL_CUSTOM_CACHE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of storage that will be used for the AWS CodeBuild project cache. Valid values: <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>, <code class="docutils literal notranslate"><span class="pre">LOCAL</span></code>, and <code class="docutils literal notranslate"><span class="pre">S3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>.</p></li>
</ul>
<p>The <strong>environment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the compute resources the build project will use. Available values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code> or <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_2XLARGE</span></code>. <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_SMALL</span></code> is only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">compute_type</span></code> need to be <code class="docutils literal notranslate"><span class="pre">BUILD_GENERAL1_LARGE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of environment variables to make available to builds for this build project.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The environment variable’s name or key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of environment variable. Valid values: <code class="docutils literal notranslate"><span class="pre">PARAMETER_STORE</span></code>, <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The environment variable’s value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Docker image to use for this build project. Valid values include <a class="reference external" href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html">Docker images provided by CodeBuild</a> (e.g <code class="docutils literal notranslate"><span class="pre">aws/codebuild/standard:2.0</span></code>), <a class="reference external" href="https://hub.docker.com/">Docker Hub images</a> (e.g. <code class="docutils literal notranslate"><span class="pre">nginx:latest</span></code>), and full Docker repository URIs such as those for ECR (e.g. <code class="docutils literal notranslate"><span class="pre">137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imagePullCredentialsType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code> or <code class="docutils literal notranslate"><span class="pre">SERVICE_ROLE</span></code>. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to <code class="docutils literal notranslate"><span class="pre">CODEBUILD</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privilegedMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, enables running the Docker daemon inside a Docker container. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryCredential</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credential</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build environment to use for related builds. Available values are: <code class="docutils literal notranslate"><span class="pre">LINUX_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">LINUX_GPU_CONTAINER</span></code>, <code class="docutils literal notranslate"><span class="pre">WINDOWS_CONTAINER</span></code> or <code class="docutils literal notranslate"><span class="pre">ARM_CONTAINER</span></code>.</p></li>
</ul>
<p>The <strong>logs_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for the builds to store logs to CloudWatch</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name of the logs in CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Current status of logs in S3 for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The stream name of the logs in CloudWatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3Logs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for the builds to store logs to S3.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Current status of logs in CloudWatch Logs for a build project. Valid values: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>secondary_artifacts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">artifactIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, output artifacts will not be encrypted. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the build output artifact location. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> then this value will be ignored. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output bucket. If <code class="docutils literal notranslate"><span class="pre">path</span></code> is not also specified, then <code class="docutils literal notranslate"><span class="pre">location</span></code> can also specify the path of the output artifact in the output bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the project. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the name of the output artifact object</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace to use in storing build artifacts. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, then valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">BUILD_ID</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideArtifactName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, a name specified in the build spec file overrides the artifact name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">packaging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of build output artifact to create. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">ZIP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">S3</span></code>, this is the path to the output artifact</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build output artifact’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">NO_ARTIFACTS</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>secondary_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build spec declaration to use for this build project’s related builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when your source provider is <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, or <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">S3</span></code>.</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource value that applies to the specified authorization type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization type to use. The only valid value is <code class="docutils literal notranslate"><span class="pre">OAUTH</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildspec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The build spec declaration to use for this build project’s related builds. This must be set when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitCloneDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Truncate git history to this many commits.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitSubmodulesConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fetchSubmodules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, fetches Git submodules for the AWS CodeBuild build project.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Ignore SSL warnings when connecting to source control.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the source code from git or s3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reportBuildStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to report the status of a build’s start and finish to your source provider. This option is only valid when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code> or <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository that contains the source code to be built. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">CODECOMMIT</span></code>, <code class="docutils literal notranslate"><span class="pre">CODEPIPELINE</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">BITBUCKET</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code> or <code class="docutils literal notranslate"><span class="pre">NO_SOURCE</span></code>.</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security group IDs to assign to running builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The subnet IDs within which to run builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the VPC within which to run builds.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.SourceCredential">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">SourceCredential</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of Source Credential.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.auth_type">
<code class="sig-name descname">auth_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.auth_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.server_type">
<code class="sig-name descname">server_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The source provider used for this project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.token" title="Permalink to this definition">¶</a></dt>
<dd><p>For <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">GitHub</span> <span class="pre">Enterprise</span></code>, this is the personal access token. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>, this is the app password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.SourceCredential.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Bitbucket username when the authType is <code class="docutils literal notranslate"><span class="pre">BASIC_AUTH</span></code>. This parameter is not valid for other types of source providers or connections.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.SourceCredential.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SourceCredential resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of Source Credential.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.</p></li>
<li><p><strong>server_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source provider used for this project.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">GitHub</span> <span class="pre">Enterprise</span></code>, this is the personal access token. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>, this is the app password.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Bitbucket username when the authType is <code class="docutils literal notranslate"><span class="pre">BASIC_AUTH</span></code>. This parameter is not valid for other types of source providers or connections.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.SourceCredential.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.SourceCredential.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.SourceCredential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Webhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codebuild.</code><code class="sig-name descname">Webhook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>filter_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A webhook filter for the group. Filter blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludeMatchedPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the specified filter does <em>not</em> trigger a build. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For a filter that uses <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> type, a comma-separated string that specifies one event: <code class="docutils literal notranslate"><span class="pre">PUSH</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_CREATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_REOPENED</span></code>. <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_MERGED</span></code> works with GitHub &amp; GitHub Enterprise only. For a filter that uses any of the other filter types, a regular expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The webhook filter group’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">EVENT</span></code>, <code class="docutils literal notranslate"><span class="pre">BASE_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTOR_ACCOUNT_ID</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_PATH</span></code>. At least one filter group must specify <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> as its type.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.branch_filter">
<code class="sig-name descname">branch_filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.branch_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use <code class="docutils literal notranslate"><span class="pre">filter_group</span></code> over <code class="docutils literal notranslate"><span class="pre">branch_filter</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.filter_groups">
<code class="sig-name descname">filter_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.filter_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the webhook’s trigger. Filter group blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A webhook filter for the group. Filter blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludeMatchedPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the specified filter does <em>not</em> trigger a build. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For a filter that uses <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> type, a comma-separated string that specifies one event: <code class="docutils literal notranslate"><span class="pre">PUSH</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_CREATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_REOPENED</span></code>. <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_MERGED</span></code> works with GitHub &amp; GitHub Enterprise only. For a filter that uses any of the other filter types, a regular expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The webhook filter group’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">EVENT</span></code>, <code class="docutils literal notranslate"><span class="pre">BASE_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTOR_ACCOUNT_ID</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_PATH</span></code>. At least one filter group must specify <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> as its type.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.payload_url">
<code class="sig-name descname">payload_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.payload_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodeBuild endpoint where webhook events are sent.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.project_name">
<code class="sig-name descname">project_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the build project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.secret">
<code class="sig-name descname">secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret token of the associated repository. Not returned by the CodeBuild API for all source types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codebuild.Webhook.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the webhook.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.Webhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payload_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Webhook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use <code class="docutils literal notranslate"><span class="pre">filter_group</span></code> over <code class="docutils literal notranslate"><span class="pre">branch_filter</span></code>.</p></li>
<li><p><strong>filter_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the webhook’s trigger. Filter group blocks are documented below.</p></li>
<li><p><strong>payload_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CodeBuild endpoint where webhook events are sent.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build project.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret token of the associated repository. Not returned by the CodeBuild API for all source types.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the webhook.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filter_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A webhook filter for the group. Filter blocks are documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludeMatchedPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the specified filter does <em>not</em> trigger a build. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For a filter that uses <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> type, a comma-separated string that specifies one event: <code class="docutils literal notranslate"><span class="pre">PUSH</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_CREATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_REOPENED</span></code>. <code class="docutils literal notranslate"><span class="pre">PULL_REQUEST_MERGED</span></code> works with GitHub &amp; GitHub Enterprise only. For a filter that uses any of the other filter types, a regular expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The webhook filter group’s type. Valid values for this parameter are: <code class="docutils literal notranslate"><span class="pre">EVENT</span></code>, <code class="docutils literal notranslate"><span class="pre">BASE_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD_REF</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTOR_ACCOUNT_ID</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_PATH</span></code>. At least one filter group must specify <code class="docutils literal notranslate"><span class="pre">EVENT</span></code> as its type.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codebuild.Webhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codebuild.Webhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codebuild.Webhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
