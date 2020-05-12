---
title: Module edas
title_tag: Module edas | Package pulumi_alicloud | Python SDK
linktitle: edas
notitle: true
---

<div class="section" id="edas">
<h1>edas<a class="headerlink" href="#edas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.edas"></span><dl class="py class">
<dt id="pulumi_alicloud.edas.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">build_pack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriotion</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecu_infos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">war_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS application resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">application_name</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">cluster_id</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">package_type</span><span class="o">=</span><span class="s2">&quot;JAR&quot;</span><span class="p">,</span>
    <span class="n">build_pack_id</span><span class="o">=</span><span class="n">xxx</span><span class="p">,</span>
    <span class="n">descriotion</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">health_check_url</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">logical_region_id</span><span class="o">=</span><span class="s2">&quot;cn-xxxx:xxx&quot;</span><span class="p">,</span>
    <span class="n">component_ids</span><span class="o">=</span><span class="n">xxx</span><span class="p">,</span>
    <span class="n">ecu_infos</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;xxx&quot;</span><span class="p">],</span>
    <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">package_version</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">war_url</span><span class="o">=</span><span class="s2">&quot;http://xxx&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of your EDAS application. Only letters ‘-‘ ‘<a href="#id3"><span class="problematic" id="id4">*</span></a>’ and numbers are allowed. The length cannot exceed 36 characters.</p>
</p></li>
<li><p><strong>build_pack_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The package ID of Enterprise Distributed Application Service (EDAS) Container, which can be retrieved by calling container version list interface ListBuildPack or the “Pack ID” column in container version list. When creating High-speed Service Framework (HSF) application, this parameter is required.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the cluster that you want to create the application. The default cluster will be used if you do not specify this parameter.</p></li>
<li><p><strong>descriotion</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the application that you want to create.</p></li>
<li><p><strong>ecu_infos</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p></li>
<li><p><strong>health_check_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for health checking of the application.</p></li>
<li><p><strong>logical_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p></li>
<li><p><strong>package_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the package for the deployment of the application that you want to create. The valid values are: WAR and JAR. We strongly recommend you to set this parameter when creating the application.</p></li>
<li><p><strong>package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p></li>
<li><p><strong>war_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.application_name">
<code class="sig-name descname">application_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.application_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your EDAS application. Only letters ‘-‘ ‘_’ and numbers are allowed. The length cannot exceed 36 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.build_pack_id">
<code class="sig-name descname">build_pack_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.build_pack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The package ID of Enterprise Distributed Application Service (EDAS) Container, which can be retrieved by calling container version list interface ListBuildPack or the “Pack ID” column in container version list. When creating High-speed Service Framework (HSF) application, this parameter is required.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the cluster that you want to create the application. The default cluster will be used if you do not specify this parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.descriotion">
<code class="sig-name descname">descriotion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.descriotion" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the application that you want to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.ecu_infos">
<code class="sig-name descname">ecu_infos</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.ecu_infos" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.group_id">
<code class="sig-name descname">group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.health_check_url">
<code class="sig-name descname">health_check_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.health_check_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for health checking of the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.logical_region_id">
<code class="sig-name descname">logical_region_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.logical_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.package_type">
<code class="sig-name descname">package_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.package_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the package for the deployment of the application that you want to create. The valid values are: WAR and JAR. We strongly recommend you to set this parameter when creating the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.package_version">
<code class="sig-name descname">package_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.package_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Application.war_url">
<code class="sig-name descname">war_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Application.war_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">build_pack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriotion</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecu_infos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">war_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of your EDAS application. Only letters ‘-‘ ‘<a href="#id7"><span class="problematic" id="id8">*</span></a>’ and numbers are allowed. The length cannot exceed 36 characters.</p>
</p></li>
<li><p><strong>build_pack_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The package ID of Enterprise Distributed Application Service (EDAS) Container, which can be retrieved by calling container version list interface ListBuildPack or the “Pack ID” column in container version list. When creating High-speed Service Framework (HSF) application, this parameter is required.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the cluster that you want to create the application. The default cluster will be used if you do not specify this parameter.</p></li>
<li><p><strong>descriotion</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the application that you want to create.</p></li>
<li><p><strong>ecu_infos</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p></li>
<li><p><strong>health_check_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for health checking of the application.</p></li>
<li><p><strong>logical_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p></li>
<li><p><strong>package_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the package for the deployment of the application that you want to create. The valid values are: WAR and JAR. We strongly recommend you to set this parameter when creating the application.</p></li>
<li><p><strong>package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p></li>
<li><p><strong>war_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.ApplicationDeployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">ApplicationDeployment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">war_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS application deployment resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">ApplicationDeployment</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">app_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;app_id&quot;</span><span class="p">],</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;group_id&quot;</span><span class="p">],</span>
    <span class="n">package_version</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;package_version&quot;</span><span class="p">],</span>
    <span class="n">war_url</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;war_url&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p></li>
<li><p><strong>package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p></li>
<li><p><strong>war_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.app_id">
<code class="sig-name descname">app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application that you want to deploy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.group_id">
<code class="sig-name descname">group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.last_package_version">
<code class="sig-name descname">last_package_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.last_package_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Last package version deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.package_version">
<code class="sig-name descname">package_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.package_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.war_url">
<code class="sig-name descname">war_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.war_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">war_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationDeployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.</p></li>
<li><p><strong>last_package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last package version deployed.</p></li>
<li><p><strong>package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.</p></li>
<li><p><strong>war_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.ApplicationDeployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.ApplicationDeployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationDeployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.ApplicationScale">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">ApplicationScale</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deploy_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecu_infos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS application scale resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">ApplicationScale</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">app_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;app_id&quot;</span><span class="p">],</span>
    <span class="n">deploy_group</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;deploy_group&quot;</span><span class="p">],</span>
    <span class="n">ecu_infos</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;ecu_info&quot;</span><span class="p">],</span>
    <span class="n">force_status</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;force_status&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>deploy_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group to which you want to add ECS instances to scale out the application.</p></li>
<li><p><strong>ecu_infos</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p></li>
<li><p><strong>force_status</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter specifies whether to forcibly remove an ECS instance where the application is deployed. It is set as true only after the ECS instance expires. In normal cases, this parameter do not need to be specified.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationScale.app_id">
<code class="sig-name descname">app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application that you want to deploy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationScale.deploy_group">
<code class="sig-name descname">deploy_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.deploy_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance group to which you want to add ECS instances to scale out the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationScale.ecc_info">
<code class="sig-name descname">ecc_info</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.ecc_info" title="Permalink to this definition">¶</a></dt>
<dd><p>The ecc information of the resource supplied above. The value is formulated as <code class="docutils literal notranslate"><span class="pre">&lt;ecc1,ecc2&gt;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationScale.ecu_infos">
<code class="sig-name descname">ecu_infos</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.ecu_infos" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.ApplicationScale.force_status">
<code class="sig-name descname">force_status</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.force_status" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter specifies whether to forcibly remove an ECS instance where the application is deployed. It is set as true only after the ECS instance expires. In normal cases, this parameter do not need to be specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.ApplicationScale.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deploy_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecc_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecu_infos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationScale resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>deploy_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance group to which you want to add ECS instances to scale out the application.</p></li>
<li><p><strong>ecc_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ecc information of the resource supplied above. The value is formulated as <code class="docutils literal notranslate"><span class="pre">&lt;ecc1,ecc2&gt;</span></code>.</p></li>
<li><p><strong>ecu_infos</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.</p></li>
<li><p><strong>force_status</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter specifies whether to forcibly remove an ECS instance where the application is deployed. It is set as true only after the ECS instance expires. In normal cases, this parameter do not need to be specified.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.ApplicationScale.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.ApplicationScale.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.ApplicationScale.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.AwaitableGetApplicationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">AwaitableGetApplicationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.AwaitableGetApplicationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.AwaitableGetDeployGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">AwaitableGetDeployGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.AwaitableGetDeployGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS cluster resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cluster_name&quot;</span><span class="p">],</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cluster_type&quot;</span><span class="p">],</span>
    <span class="n">network_mode</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;network_mode&quot;</span><span class="p">],</span>
    <span class="n">logical_region_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;logical_region_id&quot;</span><span class="p">],</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster that you want to create.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The type of the cluster that you want to create. Valid values only: 2: ECS cluster.</p></li>
<li><p><strong>logical_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Private Cloud (VPC) for the cluster.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Cluster.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster that you want to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Cluster.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the cluster that you want to create. Valid values only: 2: ECS cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Cluster.logical_region_id">
<code class="sig-name descname">logical_region_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.logical_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Cluster.network_mode">
<code class="sig-name descname">network_mode</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.network_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.Cluster.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Private Cloud (VPC) for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster that you want to create.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The type of the cluster that you want to create. Valid values only: 2: ECS cluster.</p></li>
<li><p><strong>logical_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Private Cloud (VPC) for the cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.DeployGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">DeployGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS deploy group resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">DeployGroup</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">app_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;app_id&quot;</span><span class="p">],</span>
    <span class="n">group_name</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;group_name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance group that you want to create.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.DeployGroup.app_id">
<code class="sig-name descname">app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application that you want to deploy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.DeployGroup.group_name">
<code class="sig-name descname">group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance group that you want to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.DeployGroup.group_type">
<code class="sig-name descname">group_type</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.group_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the instance group that you want to create. Valid values: 0: Default group. 1: Phased release is disabled for traffic management. 2: Phased release is enabled for traffic management.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.DeployGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeployGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application that you want to deploy.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance group that you want to create.</p></li>
<li><p><strong>group_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The type of the instance group that you want to create. Valid values: 0: Default group. 1: Phased release is disabled for traffic management. 2: Phased release is enabled for traffic management.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.DeployGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.DeployGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.DeployGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.GetApplicationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">GetApplicationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.GetApplicationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplications.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetApplicationsResult.applications">
<code class="sig-name descname">applications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetApplicationsResult.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetApplicationsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetApplicationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetApplicationsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetApplicationsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of application IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetApplicationsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetApplicationsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applications names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of clusters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cluster IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cluster names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.GetDeployGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">GetDeployGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.GetDeployGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDeployGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetDeployGroupsResult.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetDeployGroupsResult.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application that you want to deploy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetDeployGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetDeployGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of consumer group ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetDeployGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetDeployGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.GetDeployGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.GetDeployGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of deploy group names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">InstanceClusterAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS instance cluster attachment resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">InstanceClusterAttachment</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">cluster_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cluster_id&quot;</span><span class="p">],</span>
    <span class="n">instance_ids</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;instance_ids&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the cluster that you want to create the application.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of instance. Type: list.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the cluster that you want to create the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.cluster_member_ids">
<code class="sig-name descname">cluster_member_ids</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.cluster_member_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster members map of the resource supplied above. The key is instance_id and the value is cluster_member_id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.ecu_map">
<code class="sig-name descname">ecu_map</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.ecu_map" title="Permalink to this definition">¶</a></dt>
<dd><p>The ecu map of the resource supplied above. The key is instance_id and the value is ecu_id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of instance. Type: list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.status_map">
<code class="sig-name descname">status_map</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.status_map" title="Permalink to this definition">¶</a></dt>
<dd><p>The status map of the resource supplied above. The key is instance_id and the values are 1(running) 0(converting) -1(failed) and -2(offline).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_member_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecu_map</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_map</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceClusterAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the cluster that you want to create the application.</p></li>
<li><p><strong>cluster_member_ids</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The cluster members map of the resource supplied above. The key is instance_id and the value is cluster_member_id.</p></li>
<li><p><strong>ecu_map</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ecu map of the resource supplied above. The key is instance_id and the value is ecu_id.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of instance. Type: list.</p></li>
<li><p><strong>status_map</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The status map of the resource supplied above. The key is instance_id and the values are 1(running) 0(converting) -1(failed) and -2(offline).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.InstanceClusterAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.InstanceClusterAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.SlbAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">SlbAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vserver_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EDAS slb application attachment resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">SlbAttachment</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">app_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;app_id&quot;</span><span class="p">],</span>
    <span class="n">slb_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;slb_id&quot;</span><span class="p">],</span>
    <span class="n">slb_ip</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;slb_ip&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;type&quot;</span><span class="p">],</span>
    <span class="n">listener_port</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;listener_port&quot;</span><span class="p">],</span>
    <span class="n">vserver_group_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vserver_group_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the applicaton to which you want to bind an SLB instance.</p></li>
<li><p><strong>listener_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The listening port for the bound SLB instance.</p></li>
<li><p><strong>slb_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SLB instance that is going to be bound.</p></li>
<li><p><strong>slb_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address that is allocated to the bound SLB instance.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the bound SLB instance.</p></li>
<li><p><strong>vserver_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual server (VServer) group associated with the intranet SLB instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.app_id">
<code class="sig-name descname">app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the applicaton to which you want to bind an SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.listener_port">
<code class="sig-name descname">listener_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.listener_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The listening port for the bound SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.slb_id">
<code class="sig-name descname">slb_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.slb_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SLB instance that is going to be bound.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.slb_ip">
<code class="sig-name descname">slb_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.slb_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address that is allocated to the bound SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.slb_status">
<code class="sig-name descname">slb_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.slb_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Running Status of SLB instance. Inactive：The instance is stopped, and listener will not monitor and foward traffic. Active：The instance is running. After the instance is created, the default state is active. Locked：The instance is locked, the instance has been owed or locked by Alibaba Cloud. Expired: The instance has expired.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the bound SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.vserver_group_id">
<code class="sig-name descname">vserver_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.vserver_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual server (VServer) group associated with the intranet SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.edas.SlbAttachment.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC related vswitch ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.SlbAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vserver_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SlbAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the applicaton to which you want to bind an SLB instance.</p></li>
<li><p><strong>listener_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The listening port for the bound SLB instance.</p></li>
<li><p><strong>slb_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SLB instance that is going to be bound.</p></li>
<li><p><strong>slb_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address that is allocated to the bound SLB instance.</p></li>
<li><p><strong>slb_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Running Status of SLB instance. Inactive：The instance is stopped, and listener will not monitor and foward traffic. Active：The instance is running. After the instance is created, the default state is active. Locked：The instance is locked, the instance has been owed or locked by Alibaba Cloud. Expired: The instance has expired.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the bound SLB instance.</p></li>
<li><p><strong>vserver_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual server (VServer) group associated with the intranet SLB instance.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC related vswitch ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.edas.SlbAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.SlbAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.SlbAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.edas.get_applications">
<code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">get_applications</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.get_applications" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of EDAS application in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">applications</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">get_applications</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;xxx&quot;</span><span class="p">],</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;application.txt&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstApplicationName&quot;</span><span class="p">,</span> <span class="n">applications</span><span class="o">.</span><span class="n">applications</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;appName&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – An ids string to filter results by the application id.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the application name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.edas.get_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logical_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of EDAS clusters in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">clusters</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">get_clusters</span><span class="p">(</span><span class="n">logical_region_id</span><span class="o">=</span><span class="s2">&quot;cn-shenzhen:xxx&quot;</span><span class="p">,</span>
    <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;addfs-dfsasd&quot;</span><span class="p">],</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;clusters.txt&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstClusterName&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;actiontrail.getConsumerGroups&quot;</span><span class="p">][</span><span class="s2">&quot;clusters&quot;</span><span class="p">][</span><span class="s2">&quot;clusters&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;cluster_name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – An ids string to filter results by the cluster id.</p></li>
<li><p><strong>logical_region_id</strong> (<em>str</em>) – ID of the namespace in EDAS.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.edas.get_deploy_groups">
<code class="sig-prename descclassname">pulumi_alicloud.edas.</code><code class="sig-name descname">get_deploy_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.edas.get_deploy_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of EDAS deploy groups in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">groups</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">edas</span><span class="o">.</span><span class="n">get_deploy_groups</span><span class="p">(</span><span class="n">app_id</span><span class="o">=</span><span class="s2">&quot;xxx&quot;</span><span class="p">,</span>
    <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;xxx&quot;</span><span class="p">],</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;groups.txt&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstGroupName&quot;</span><span class="p">,</span> <span class="n">groups</span><span class="o">.</span><span class="n">groups</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;group_name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>app_id</strong> (<em>str</em>) – ID of the EDAS application.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the deploy group name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
