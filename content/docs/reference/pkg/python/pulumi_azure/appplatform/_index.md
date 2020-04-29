---
title: Module appplatform
title_tag: Module appplatform | Package pulumi_azure | Python SDK
linktitle: appplatform
notitle: true
---

<div class="section" id="appplatform">
<h1>appplatform<a class="headerlink" href="#appplatform" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.appplatform"></span><dl class="class">
<dt id="pulumi_azure.appplatform.AwaitableGetSpringCloudServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appplatform.</code><code class="sig-name descname">AwaitableGetSpringCloudServiceResult</code><span class="sig-paren">(</span><em class="sig-param">config_server_git_settings=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.AwaitableGetSpringCloudServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appplatform.</code><code class="sig-name descname">GetSpringCloudServiceResult</code><span class="sig-paren">(</span><em class="sig-param">config_server_git_settings=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpringCloudService.</p>
<dl class="attribute">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult.config_server_git_settings">
<code class="sig-name descname">config_server_git_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult.config_server_git_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">config_server_git_setting</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of Spring Cloud Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify on the Git repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.GetSpringCloudServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.GetSpringCloudServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to Spring Cloud Service.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appplatform.SpringCloudApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appplatform.</code><code class="sig-name descname">SpringCloudApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Spring Cloud Application.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudApp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudApp.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudApp.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appplatform.SpringCloudApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpringCloudApp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appplatform.SpringCloudApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appplatform.SpringCloudApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appplatform.SpringCloudService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appplatform.</code><code class="sig-name descname">SpringCloudService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config_server_git_setting=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Spring Cloud Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_server_git_setting</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">config_server_git_setting</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies The name of the resource group in which to create the Spring Cloud Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config_server_git_setting</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">repository</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name to identify on the Git repository, required only if repos exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to match an application name. For each pattern, use the <code class="docutils literal notranslate"><span class="pre">{application}/{profile}</span></code> format with wildcards.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the Git repository that’s used as the Config Server back end should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the default Git repository used as the Config Server back end, should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudService.config_server_git_setting">
<code class="sig-name descname">config_server_git_setting</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.config_server_git_setting" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">config_server_git_setting</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositories</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">repository</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A name to identify on the Git repository, required only if repos exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patterns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of strings used to match an application name. For each pattern, use the <code class="docutils literal notranslate"><span class="pre">{application}/{profile}</span></code> format with wildcards.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI of the Git repository that’s used as the Config Server back end should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI of the default Git repository used as the Config Server back end, should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudService.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudService.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies The name of the resource group in which to create the Spring Cloud Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appplatform.SpringCloudService.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appplatform.SpringCloudService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config_server_git_setting=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpringCloudService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_server_git_setting</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">config_server_git_setting</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies The name of the resource group in which to create the Spring Cloud Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config_server_git_setting</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">repository</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_basic_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that’s used to access the Git repository server, required when the Git repository server supports Http Basic Authentication.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name to identify on the Git repository, required only if repos exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to match an application name. For each pattern, use the <code class="docutils literal notranslate"><span class="pre">{application}/{profile}</span></code> format with wildcards.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the Git repository that’s used as the Config Server back end should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">searchPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings used to search subdirectories of the Git repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">ssh_auth</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key of the Git repository server, should not include the algorithm prefix as covered by <code class="docutils literal notranslate"><span class="pre">host-key-algorithm</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostKeyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The host key algorithm, should be <code class="docutils literal notranslate"><span class="pre">ssh-dss</span></code>, <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp256</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp384</span></code>, or <code class="docutils literal notranslate"><span class="pre">ecdsa-sha2-nistp521</span></code>. Required only if <code class="docutils literal notranslate"><span class="pre">host-key</span></code> exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSH private key to access the Git repository, required when the URI starts with <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code> or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strictHostKeyCheckingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the Config Server instance will fail to start if the host_key does not match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the default Git repository used as the Config Server back end, should be started with <code class="docutils literal notranslate"><span class="pre">http://</span></code>, <code class="docutils literal notranslate"><span class="pre">https://</span></code>, <code class="docutils literal notranslate"><span class="pre">git&#64;</span></code>, or <code class="docutils literal notranslate"><span class="pre">ssh://</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appplatform.SpringCloudService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appplatform.SpringCloudService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.SpringCloudService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appplatform.get_spring_cloud_service">
<code class="sig-prename descclassname">pulumi_azure.appplatform.</code><code class="sig-name descname">get_spring_cloud_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appplatform.get_spring_cloud_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Spring Cloud Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies The name of the Spring Cloud Service resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the Spring Cloud Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
