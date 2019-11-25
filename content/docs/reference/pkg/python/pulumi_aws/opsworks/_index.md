---
title: Module opsworks
linktitle: opsworks
notitle: true
---

<div class="section" id="opsworks">
<h1>opsworks<a class="headerlink" href="#opsworks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.opsworks"></span><dl class="class">
<dt id="pulumi_aws.opsworks.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_sources=None</em>, <em class="sig-param">auto_bundle_on_deploy=None</em>, <em class="sig-param">aws_flow_ruby_settings=None</em>, <em class="sig-param">data_source_arn=None</em>, <em class="sig-param">data_source_database_name=None</em>, <em class="sig-param">data_source_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">document_root=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">enable_ssl=None</em>, <em class="sig-param">environments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rails_env=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">ssl_configurations=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks application resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SCM configuration of the app as described below.</p></li>
<li><p><strong>auto_bundle_on_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>aws_flow_ruby_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify activity and workflow workers for your app using the aws-flow gem.</p></li>
<li><p><strong>data_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s ARN.</p></li>
<li><p><strong>data_source_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database name.</p></li>
<li><p><strong>data_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the app.</p></li>
<li><p><strong>document_root</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual host alias.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p></li>
<li><p><strong>environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object to define environment variables.  Object is described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the application.</p></li>
<li><p><strong>rails_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p></li>
<li><p><strong>ssl_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The SSL configuration of the app. Object is described below.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the application will belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source to use. For example, “archive”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
<p>The <strong>environments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.app_sources">
<code class="sig-name descname">app_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.app_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>SCM configuration of the app as described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.auto_bundle_on_deploy">
<code class="sig-name descname">auto_bundle_on_deploy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.auto_bundle_on_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.aws_flow_ruby_settings">
<code class="sig-name descname">aws_flow_ruby_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.aws_flow_ruby_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify activity and workflow workers for your app using the aws-flow gem.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_arn">
<code class="sig-name descname">data_source_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_database_name">
<code class="sig-name descname">data_source_database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The database name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_type">
<code class="sig-name descname">data_source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.document_root">
<code class="sig-name descname">document_root</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.document_root" title="Permalink to this definition">¶</a></dt>
<dd><p>Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.domains">
<code class="sig-name descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of virtual host alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.enable_ssl">
<code class="sig-name descname">enable_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.enable_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.environments">
<code class="sig-name descname">environments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Object to define environment variables.  Object is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.rails_env">
<code class="sig-name descname">rails_env</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.rails_env" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.ssl_configurations">
<code class="sig-name descname">ssl_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.ssl_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL configuration of the app. Object is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the application will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source to use. For example, “archive”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_sources=None</em>, <em class="sig-param">auto_bundle_on_deploy=None</em>, <em class="sig-param">aws_flow_ruby_settings=None</em>, <em class="sig-param">data_source_arn=None</em>, <em class="sig-param">data_source_database_name=None</em>, <em class="sig-param">data_source_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">document_root=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">enable_ssl=None</em>, <em class="sig-param">environments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rails_env=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">ssl_configurations=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SCM configuration of the app as described below.</p></li>
<li><p><strong>auto_bundle_on_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>aws_flow_ruby_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify activity and workflow workers for your app using the aws-flow gem.</p></li>
<li><p><strong>data_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s ARN.</p></li>
<li><p><strong>data_source_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database name.</p></li>
<li><p><strong>data_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the app.</p></li>
<li><p><strong>document_root</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual host alias.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p></li>
<li><p><strong>environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object to define environment variables.  Object is described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the application.</p></li>
<li><p><strong>rails_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p></li>
<li><p><strong>ssl_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The SSL configuration of the app. Object is described below.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the application will belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source to use. For example, “archive”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
<p>The <strong>environments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.CustomLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">CustomLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks custom layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_custom_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_custom_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.CustomLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_custom_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_custom_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.CustomLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.CustomLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.GangliaLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">GangliaLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ganglia layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for Ganglia.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to use for Ganglia. Defaults to “/ganglia”.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for Ganglia. Defaults to “opsworks”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_ganglia_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_ganglia_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for Ganglia.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to use for Ganglia. Defaults to “/ganglia”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username to use for Ganglia. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.GangliaLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GangliaLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for Ganglia.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to use for Ganglia. Defaults to “/ganglia”.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for Ganglia. Defaults to “opsworks”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_ganglia_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_ganglia_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.HaproxyLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">HaproxyLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">healthcheck_method=None</em>, <em class="sig-param">healthcheck_url=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">stats_enabled=None</em>, <em class="sig-param">stats_password=None</em>, <em class="sig-param">stats_url=None</em>, <em class="sig-param">stats_user=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks haproxy layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>healthcheck_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p></li>
<li><p><strong>healthcheck_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL path to use for instance healthchecks. Defaults to “/”.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>stats_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable HAProxy stats.</p></li>
<li><p><strong>stats_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for HAProxy stats.</p></li>
<li><p><strong>stats_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HAProxy stats URL. Defaults to “/haproxy?stats”.</p></li>
<li><p><strong>stats_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for HAProxy stats. Defaults to “opsworks”.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_haproxy_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_haproxy_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_method">
<code class="sig-name descname">healthcheck_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_method" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_url">
<code class="sig-name descname">healthcheck_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL path to use for instance healthchecks. Defaults to “/”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_enabled">
<code class="sig-name descname">stats_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable HAProxy stats.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_password">
<code class="sig-name descname">stats_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for HAProxy stats.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_url">
<code class="sig-name descname">stats_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The HAProxy stats URL. Defaults to “/haproxy?stats”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_user">
<code class="sig-name descname">stats_user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The username for HAProxy stats. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">healthcheck_method=None</em>, <em class="sig-param">healthcheck_url=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">stats_enabled=None</em>, <em class="sig-param">stats_password=None</em>, <em class="sig-param">stats_url=None</em>, <em class="sig-param">stats_user=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HaproxyLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>healthcheck_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p></li>
<li><p><strong>healthcheck_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL path to use for instance healthchecks. Defaults to “/”.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>stats_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable HAProxy stats.</p></li>
<li><p><strong>stats_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for HAProxy stats.</p></li>
<li><p><strong>stats_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HAProxy stats URL. Defaults to “/haproxy?stats”.</p></li>
<li><p><strong>stats_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for HAProxy stats. Defaults to “opsworks”.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_haproxy_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_haproxy_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">ami_id=None</em>, <em class="sig-param">architecture=None</em>, <em class="sig-param">auto_scaling_type=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">delete_ebs=None</em>, <em class="sig-param">delete_eip=None</em>, <em class="sig-param">ebs_block_devices=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">ecs_cluster_arn=None</em>, <em class="sig-param">elastic_ip=None</em>, <em class="sig-param">ephemeral_block_devices=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">infrastructure_class=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_profile_arn=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">last_service_error_id=None</em>, <em class="sig-param">layer_ids=None</em>, <em class="sig-param">os=None</em>, <em class="sig-param">platform=None</em>, <em class="sig-param">private_dns=None</em>, <em class="sig-param">private_ip=None</em>, <em class="sig-param">public_dns=None</em>, <em class="sig-param">public_ip=None</em>, <em class="sig-param">registered_by=None</em>, <em class="sig-param">reported_agent_version=None</em>, <em class="sig-param">reported_os_family=None</em>, <em class="sig-param">reported_os_name=None</em>, <em class="sig-param">reported_os_version=None</em>, <em class="sig-param">root_block_devices=None</em>, <em class="sig-param">root_device_type=None</em>, <em class="sig-param">root_device_volume_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">ssh_host_dsa_key_fingerprint=None</em>, <em class="sig-param">ssh_host_rsa_key_fingerprint=None</em>, <em class="sig-param">ssh_key_name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tenancy=None</em>, <em class="sig-param">virtualization_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks instance resource.</p>
<p>Each of the <code class="docutils literal notranslate"><span class="pre">*_block_device</span></code> attributes controls a portion of the AWS
Instance’s “Block Device Mapping”. It’s a good idea to familiarize yourself with <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">AWS’s Block Device
Mapping docs</a>
to understand the implications of using these attributes.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">root_block_device</span></code> mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> - (Optional) The type of volume. Can be <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;gp2&quot;</span></code>,
or <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> - (Optional) The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> - (Optional) The amount of provisioned
<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html">IOPS</a>.
This must be set with a <code class="docutils literal notranslate"><span class="pre">volume_type</span></code> of <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_on_termination</span></code> - (Optional) Whether the volume should be destroyed
on instance termination (Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
</ul>
<p>Modifying any of the <code class="docutils literal notranslate"><span class="pre">root_block_device</span></code> settings requires resource
replacement.</p>
<p>Each <code class="docutils literal notranslate"><span class="pre">ebs_block_device</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> - The name of the device to mount.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> - (Optional) The Snapshot ID to mount.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> - (Optional) The type of volume. Can be <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;gp2&quot;</span></code>,
or <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> - (Optional) The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> - (Optional) The amount of provisioned
<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html">IOPS</a>.
This must be set with a <code class="docutils literal notranslate"><span class="pre">volume_type</span></code> of <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_on_termination</span></code> - (Optional) Whether the volume should be destroyed
on instance termination (Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
</ul>
<p>Modifying any <code class="docutils literal notranslate"><span class="pre">ebs_block_device</span></code> currently requires resource replacement.</p>
<p>Each <code class="docutils literal notranslate"><span class="pre">ephemeral_block_device</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> - The name of the block device to mount on the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_name</span></code> - The <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames">Instance Store Device
Name</a>
(e.g. <code class="docutils literal notranslate"><span class="pre">&quot;ephemeral0&quot;</span></code>)</p></li>
</ul>
<p>Each AWS Instance type has a different set of Instance Store block devices
available for attachment. AWS <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes">publishes a
list</a>
of which ephemeral devices are available on each type. The devices are always
identified by the <code class="docutils literal notranslate"><span class="pre">virtual_name</span></code> in the format <code class="docutils literal notranslate"><span class="pre">&quot;ephemeral{0..N}&quot;</span></code>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Currently, changes to <code class="docutils literal notranslate"><span class="pre">*_block_device</span></code> configuration of <em>existing</em>
resources cannot be automatically detected by this provider. After making updates
to block device configuration, resource recreation can be manually triggered by
using the <cite>``taint`</cite> command &lt;<a class="reference external" href="https://www.terraform.io/docs/commands/taint.html">https://www.terraform.io/docs/commands/taint.html</a>&gt;`_.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p></li>
<li><p><strong>ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p></li>
<li><p><strong>auto_scaling_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default.</p></li>
<li><p><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</p></li>
<li><p><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance’s host name.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start</p></li>
<li><p><strong>layer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ids of the layers the instance will belong to.</p></li>
<li><p><strong>os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of operating system that will be installed.</p></li>
<li><p><strong>private_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address assigned to the instance</p></li>
<li><p><strong>public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address assigned to the instance, if applicable.</p></li>
<li><p><strong>root_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</p></li>
<li><p><strong>root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the instance will belong to.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to attach to</p></li>
<li><p><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p></li>
<li><p><strong>virtualization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>root_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.agent_version">
<code class="sig-name descname">agent_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ami_id">
<code class="sig-name descname">ami_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.architecture">
<code class="sig-name descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.auto_scaling_type">
<code class="sig-name descname">auto_scaling_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.auto_scaling_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_block_devices">
<code class="sig-name descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ec2_instance_id">
<code class="sig-name descname">ec2_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ec2_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 instance ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ephemeral_block_devices">
<code class="sig-name descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance’s host name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.layer_ids">
<code class="sig-name descname">layer_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.layer_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids of the layers the instance will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.os">
<code class="sig-name descname">os</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of operating system that will be installed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.private_dns">
<code class="sig-name descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address assigned to the instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.public_dns">
<code class="sig-name descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.public_ip">
<code class="sig-name descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the instance, if applicable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.root_block_devices">
<code class="sig-name descname">root_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.root_device_type">
<code class="sig-name descname">root_device_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ssh_key_name">
<code class="sig-name descname">ssh_key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the instance will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet ID to attach to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.tenancy">
<code class="sig-name descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.virtualization_type">
<code class="sig-name descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">ami_id=None</em>, <em class="sig-param">architecture=None</em>, <em class="sig-param">auto_scaling_type=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">delete_ebs=None</em>, <em class="sig-param">delete_eip=None</em>, <em class="sig-param">ebs_block_devices=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">ec2_instance_id=None</em>, <em class="sig-param">ecs_cluster_arn=None</em>, <em class="sig-param">elastic_ip=None</em>, <em class="sig-param">ephemeral_block_devices=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">infrastructure_class=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_profile_arn=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">last_service_error_id=None</em>, <em class="sig-param">layer_ids=None</em>, <em class="sig-param">os=None</em>, <em class="sig-param">platform=None</em>, <em class="sig-param">private_dns=None</em>, <em class="sig-param">private_ip=None</em>, <em class="sig-param">public_dns=None</em>, <em class="sig-param">public_ip=None</em>, <em class="sig-param">registered_by=None</em>, <em class="sig-param">reported_agent_version=None</em>, <em class="sig-param">reported_os_family=None</em>, <em class="sig-param">reported_os_name=None</em>, <em class="sig-param">reported_os_version=None</em>, <em class="sig-param">root_block_devices=None</em>, <em class="sig-param">root_device_type=None</em>, <em class="sig-param">root_device_volume_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">ssh_host_dsa_key_fingerprint=None</em>, <em class="sig-param">ssh_host_rsa_key_fingerprint=None</em>, <em class="sig-param">ssh_key_name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tenancy=None</em>, <em class="sig-param">virtualization_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p></li>
<li><p><strong>ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p></li>
<li><p><strong>auto_scaling_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default.</p></li>
<li><p><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</p></li>
<li><p><strong>ec2_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EC2 instance ID</p></li>
<li><p><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance’s host name.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start</p></li>
<li><p><strong>layer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ids of the layers the instance will belong to.</p></li>
<li><p><strong>os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of operating system that will be installed.</p></li>
<li><p><strong>private_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address assigned to the instance</p></li>
<li><p><strong>public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address assigned to the instance, if applicable.</p></li>
<li><p><strong>root_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</p></li>
<li><p><strong>root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the instance will belong to.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to attach to</p></li>
<li><p><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p></li>
<li><p><strong>virtualization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>root_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.JavaAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">JavaAppLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_server=None</em>, <em class="sig-param">app_server_version=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">jvm_options=None</em>, <em class="sig-param">jvm_type=None</em>, <em class="sig-param">jvm_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Java application layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the application container to use. Defaults to “tomcat”.</p></li>
<li><p><strong>app_server_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the selected application container to use. Defaults to “7”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>jvm_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Options to set for the JVM.</p></li>
<li><p><strong>jvm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p></li>
<li><p><strong>jvm_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of JVM to use. Defaults to “7”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_java_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_java_app_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server">
<code class="sig-name descname">app_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the application container to use. Defaults to “tomcat”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server_version">
<code class="sig-name descname">app_server_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the selected application container to use. Defaults to “7”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_options">
<code class="sig-name descname">jvm_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options to set for the JVM.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_type">
<code class="sig-name descname">jvm_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_version">
<code class="sig-name descname">jvm_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of JVM to use. Defaults to “7”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_server=None</em>, <em class="sig-param">app_server_version=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">jvm_options=None</em>, <em class="sig-param">jvm_type=None</em>, <em class="sig-param">jvm_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JavaAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the application container to use. Defaults to “tomcat”.</p></li>
<li><p><strong>app_server_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the selected application container to use. Defaults to “7”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>jvm_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Options to set for the JVM.</p></li>
<li><p><strong>jvm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p></li>
<li><p><strong>jvm_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of JVM to use. Defaults to “7”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_java_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_java_app_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MemcachedLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">MemcachedLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_memory=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks memcached layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_memcached_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_memcached_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.allocated_memory">
<code class="sig-name descname">allocated_memory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.allocated_memory" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_memory=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MemcachedLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_memcached_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_memcached_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MysqlLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">MysqlLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">root_password=None</em>, <em class="sig-param">root_password_on_all_instances=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks MySQL layer resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the root password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to use for MySQL.</p></li>
<li><p><strong>root_password_on_all_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_mysql_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_mysql_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password">
<code class="sig-name descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to use for MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances">
<code class="sig-name descname">root_password_on_all_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MysqlLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">root_password=None</em>, <em class="sig-param">root_password_on_all_instances=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MysqlLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to use for MySQL.</p></li>
<li><p><strong>root_password_on_all_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_mysql_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_mysql_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.NodejsAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">NodejsAppLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodejs_version=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks NodeJS application layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>nodejs_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of NodeJS to use. Defaults to “0.10.38”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_nodejs_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_nodejs_app_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.nodejs_version">
<code class="sig-name descname">nodejs_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.nodejs_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of NodeJS to use. Defaults to “0.10.38”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodejs_version=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodejsAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>nodejs_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of NodeJS to use. Defaults to “0.10.38”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_nodejs_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_nodejs_app_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Permission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Permission</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_ssh=None</em>, <em class="sig-param">allow_sudo=None</em>, <em class="sig-param">level=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">user_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks permission resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use SSH to communicate with the instance</p></li>
<li><p><strong>allow_sudo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use sudo to elevate privileges</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to set the permissions for</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN to set permissions for</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_permission.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_ssh">
<code class="sig-name descname">allow_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use SSH to communicate with the instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_sudo">
<code class="sig-name descname">allow_sudo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_sudo" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use sudo to elevate privileges</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.level">
<code class="sig-name descname">level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.level" title="Permalink to this definition">¶</a></dt>
<dd><p>The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to set the permissions for</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.user_arn">
<code class="sig-name descname">user_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN to set permissions for</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Permission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_ssh=None</em>, <em class="sig-param">allow_sudo=None</em>, <em class="sig-param">level=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">user_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Permission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use SSH to communicate with the instance</p></li>
<li><p><strong>allow_sudo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use sudo to elevate privileges</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to set the permissions for</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN to set permissions for</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_permission.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Permission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Permission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.PhpAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">PhpAppLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks PHP application layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_php_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_php_app_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PhpAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_php_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_php_app_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RailsAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">RailsAppLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_server=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">bundler_version=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">manage_bundler=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">passenger_version=None</em>, <em class="sig-param">ruby_version=None</em>, <em class="sig-param">rubygems_version=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ruby on Rails application layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the app server to use. Defaults to “apache_passenger”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>bundler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>manage_bundler</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether OpsWorks should manage bundler. On by default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>passenger_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Passenger to use. Defaults to “4.0.46”.</p></li>
<li><p><strong>ruby_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Ruby to use. Defaults to “2.0.0”.</p></li>
<li><p><strong>rubygems_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of RubyGems to use. Defaults to “2.2.2”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rails_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rails_app_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.app_server">
<code class="sig-name descname">app_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the app server to use. Defaults to “apache_passenger”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.bundler_version">
<code class="sig-name descname">bundler_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.bundler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.manage_bundler">
<code class="sig-name descname">manage_bundler</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.manage_bundler" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether OpsWorks should manage bundler. On by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.passenger_version">
<code class="sig-name descname">passenger_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.passenger_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Passenger to use. Defaults to “4.0.46”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ruby_version">
<code class="sig-name descname">ruby_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ruby_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Ruby to use. Defaults to “2.0.0”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.rubygems_version">
<code class="sig-name descname">rubygems_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.rubygems_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of RubyGems to use. Defaults to “2.2.2”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_server=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">bundler_version=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">manage_bundler=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">passenger_version=None</em>, <em class="sig-param">ruby_version=None</em>, <em class="sig-param">rubygems_version=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RailsAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the app server to use. Defaults to “apache_passenger”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>bundler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>manage_bundler</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether OpsWorks should manage bundler. On by default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>passenger_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Passenger to use. Defaults to “4.0.46”.</p></li>
<li><p><strong>ruby_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Ruby to use. Defaults to “2.0.0”.</p></li>
<li><p><strong>rubygems_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of RubyGems to use. Defaults to “2.2.2”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rails_app_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rails_app_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RdsDbInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">RdsDbInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_password=None</em>, <em class="sig-param">db_user=None</em>, <em class="sig-param">rds_db_instance_arn=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks RDS DB Instance resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db password</p></li>
<li><p><strong>db_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db username</p></li>
<li><p><strong>rds_db_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db instance to register for this stack. Changing this will force a new resource.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to register a db instance for. Changing this will force a new resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rds_db_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rds_db_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_password">
<code class="sig-name descname">db_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_password" title="Permalink to this definition">¶</a></dt>
<dd><p>A db password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_user">
<code class="sig-name descname">db_user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_user" title="Permalink to this definition">¶</a></dt>
<dd><p>A db username</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn">
<code class="sig-name descname">rds_db_instance_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The db instance to register for this stack. Changing this will force a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to register a db instance for. Changing this will force a new resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_password=None</em>, <em class="sig-param">db_user=None</em>, <em class="sig-param">rds_db_instance_arn=None</em>, <em class="sig-param">stack_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RdsDbInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db password</p></li>
<li><p><strong>db_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db username</p></li>
<li><p><strong>rds_db_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db instance to register for this stack. Changing this will force a new resource.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to register a db instance for. Changing this will force a new resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rds_db_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_rds_db_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Stack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Stack</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">berkshelf_version=None</em>, <em class="sig-param">color=None</em>, <em class="sig-param">configuration_manager_name=None</em>, <em class="sig-param">configuration_manager_version=None</em>, <em class="sig-param">custom_cookbooks_sources=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">default_availability_zone=None</em>, <em class="sig-param">default_instance_profile_arn=None</em>, <em class="sig-param">default_os=None</em>, <em class="sig-param">default_root_device_type=None</em>, <em class="sig-param">default_ssh_key_name=None</em>, <em class="sig-param">default_subnet_id=None</em>, <em class="sig-param">hostname_theme=None</em>, <em class="sig-param">manage_berkshelf=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">use_custom_cookbooks=None</em>, <em class="sig-param">use_opsworks_security_groups=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks stack resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p></li>
<li><p><strong>berkshelf_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Color to paint next to the stack’s resources in the OpsWorks console.</p></li>
<li><p><strong>configuration_manager_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration manager to use. Defaults to “Chef”.</p></li>
<li><p><strong>configuration_manager_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the configuration manager to use. Defaults to “11.4”.</p></li>
<li><p><strong>custom_cookbooks_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the entire stack.</p></li>
<li><p><strong>default_availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p></li>
<li><p><strong>default_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Instance Profile that created instances
will have by default.</p></li>
<li><p><strong>default_os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of OS that will be installed on instances by default.</p></li>
<li><p><strong>default_root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.</p></li>
<li><p><strong>default_ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>default_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p></li>
<li><p><strong>hostname_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p></li>
<li><p><strong>manage_berkshelf</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stack.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the region where the stack will exist.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that the OpsWorks service will act as.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>use_custom_cookbooks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the custom cookbook settings are
enabled.</p></li>
<li><p><strong>use_opsworks_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that this stack belongs to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_cookbooks_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_stack.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.agent_version">
<code class="sig-name descname">agent_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.berkshelf_version">
<code class="sig-name descname">berkshelf_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.berkshelf_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.color">
<code class="sig-name descname">color</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.color" title="Permalink to this definition">¶</a></dt>
<dd><p>Color to paint next to the stack’s resources in the OpsWorks console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_name">
<code class="sig-name descname">configuration_manager_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration manager to use. Defaults to “Chef”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_version">
<code class="sig-name descname">configuration_manager_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the configuration manager to use. Defaults to “11.4”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_cookbooks_sources">
<code class="sig-name descname">custom_cookbooks_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_cookbooks_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_json">
<code class="sig-name descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the entire stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_availability_zone">
<code class="sig-name descname">default_availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_instance_profile_arn">
<code class="sig-name descname">default_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM Instance Profile that created instances
will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_os">
<code class="sig-name descname">default_os</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of OS that will be installed on instances by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_root_device_type">
<code class="sig-name descname">default_root_device_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_ssh_key_name">
<code class="sig-name descname">default_ssh_key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_subnet_id">
<code class="sig-name descname">default_subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.hostname_theme">
<code class="sig-name descname">hostname_theme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.hostname_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.manage_berkshelf">
<code class="sig-name descname">manage_berkshelf</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.manage_berkshelf" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the region where the stack will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that the OpsWorks service will act as.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.use_custom_cookbooks">
<code class="sig-name descname">use_custom_cookbooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_custom_cookbooks" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the custom cookbook settings are
enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.use_opsworks_security_groups">
<code class="sig-name descname">use_opsworks_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_opsworks_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that this stack belongs to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Stack.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">berkshelf_version=None</em>, <em class="sig-param">color=None</em>, <em class="sig-param">configuration_manager_name=None</em>, <em class="sig-param">configuration_manager_version=None</em>, <em class="sig-param">custom_cookbooks_sources=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">default_availability_zone=None</em>, <em class="sig-param">default_instance_profile_arn=None</em>, <em class="sig-param">default_os=None</em>, <em class="sig-param">default_root_device_type=None</em>, <em class="sig-param">default_ssh_key_name=None</em>, <em class="sig-param">default_subnet_id=None</em>, <em class="sig-param">hostname_theme=None</em>, <em class="sig-param">manage_berkshelf=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">stack_endpoint=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">use_custom_cookbooks=None</em>, <em class="sig-param">use_opsworks_security_groups=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Stack resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p></li>
<li><p><strong>berkshelf_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Color to paint next to the stack’s resources in the OpsWorks console.</p></li>
<li><p><strong>configuration_manager_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration manager to use. Defaults to “Chef”.</p></li>
<li><p><strong>configuration_manager_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the configuration manager to use. Defaults to “11.4”.</p></li>
<li><p><strong>custom_cookbooks_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the entire stack.</p></li>
<li><p><strong>default_availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p></li>
<li><p><strong>default_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Instance Profile that created instances
will have by default.</p></li>
<li><p><strong>default_os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of OS that will be installed on instances by default.</p></li>
<li><p><strong>default_root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.</p></li>
<li><p><strong>default_ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>default_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p></li>
<li><p><strong>hostname_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p></li>
<li><p><strong>manage_berkshelf</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stack.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the region where the stack will exist.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that the OpsWorks service will act as.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>use_custom_cookbooks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the custom cookbook settings are
enabled.</p></li>
<li><p><strong>use_opsworks_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that this stack belongs to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_cookbooks_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_stack.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Stack.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Stack.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.StaticWebLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">StaticWebLayer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks static web server layer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_static_web_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_static_web_layer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_assign_elastic_ips=None</em>, <em class="sig-param">auto_assign_public_ips=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">custom_configure_recipes=None</em>, <em class="sig-param">custom_deploy_recipes=None</em>, <em class="sig-param">custom_instance_profile_arn=None</em>, <em class="sig-param">custom_json=None</em>, <em class="sig-param">custom_security_group_ids=None</em>, <em class="sig-param">custom_setup_recipes=None</em>, <em class="sig-param">custom_shutdown_recipes=None</em>, <em class="sig-param">custom_undeploy_recipes=None</em>, <em class="sig-param">drain_elb_on_shutdown=None</em>, <em class="sig-param">ebs_volumes=None</em>, <em class="sig-param">elastic_load_balancer=None</em>, <em class="sig-param">install_updates_on_boot=None</em>, <em class="sig-param">instance_shutdown_timeout=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">system_packages=None</em>, <em class="sig-param">use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StaticWebLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_static_web_layer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_static_web_layer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.UserProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">UserProfile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_self_management=None</em>, <em class="sig-param">ssh_public_key=None</em>, <em class="sig-param">ssh_username=None</em>, <em class="sig-param">user_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks User Profile resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_self_management</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users can specify their own SSH public key through the My Settings page</p></li>
<li><p><strong>ssh_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users public key</p></li>
<li><p><strong>ssh_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ssh username, with witch this user wants to log in</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_user_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_user_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.allow_self_management">
<code class="sig-name descname">allow_self_management</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.allow_self_management" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether users can specify their own SSH public key through the My Settings page</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_public_key">
<code class="sig-name descname">ssh_public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The users public key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_username">
<code class="sig-name descname">ssh_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The ssh username, with witch this user wants to log in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.user_arn">
<code class="sig-name descname">user_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.UserProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_self_management=None</em>, <em class="sig-param">ssh_public_key=None</em>, <em class="sig-param">ssh_username=None</em>, <em class="sig-param">user_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_self_management</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users can specify their own SSH public key through the My Settings page</p></li>
<li><p><strong>ssh_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users public key</p></li>
<li><p><strong>ssh_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ssh username, with witch this user wants to log in</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_user_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_user_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.UserProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.UserProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
