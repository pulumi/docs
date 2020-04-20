---
title: Module cs
title_tag: Module cs | Package pulumi_alicloud | Python SDK
linktitle: cs
notitle: true
---

<div class="section" id="cs">
<h1>cs<a class="headerlink" href="#cs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cs"></span><dl class="class">
<dt id="pulumi_alicloud.cs.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">blue_green=None</em>, <em class="sig-param">blue_green_confirm=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">latest_image=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>DEPRECATED:</strong> This resource manages applications in swarm cluster only, which is being deprecated and will be replaced by Kubernetes cluster.</p>
</div></blockquote>
<p>This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
Each application can contain one or more services.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Application orchestration template must be a valid Docker Compose YAML template.</p>
<p><strong>NOTE:</strong> At present, this resource only support swarm cluster.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blue_green</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wherther to use “Blue Green” method when release a new version. Default to false.</p></li>
<li><p><strong>blue_green_confirm</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The swarm cluster’s name.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of application.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key/value map used to replace the variable parameter in the Compose template.</p></li>
<li><p><strong>latest_image</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use latest docker image while each updating application. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.blue_green">
<code class="sig-name descname">blue_green</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.blue_green" title="Permalink to this definition">¶</a></dt>
<dd><p>Wherther to use “Blue Green” method when release a new version. Default to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.blue_green_confirm">
<code class="sig-name descname">blue_green_confirm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.blue_green_confirm" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The swarm cluster’s name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.default_domain">
<code class="sig-name descname">default_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.default_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The application default domain and it can be used to configure routing service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.environment">
<code class="sig-name descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>A key/value map used to replace the variable parameter in the Compose template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.latest_image">
<code class="sig-name descname">latest_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.latest_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use latest docker image while each updating application. Default to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of services in the application. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The current status of service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Application.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The application deploying version. Each updating, it must be different with current. Default to “1.0”</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">blue_green=None</em>, <em class="sig-param">blue_green_confirm=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">default_domain=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">latest_image=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blue_green</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wherther to use “Blue Green” method when release a new version. Default to false.</p></li>
<li><p><strong>blue_green_confirm</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The swarm cluster’s name.</p></li>
<li><p><strong>default_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application default domain and it can be used to configure routing service.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of application.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key/value map used to replace the variable parameter in the Compose template.</p></li>
<li><p><strong>latest_image</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use latest docker image while each updating application. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of services in the application. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p>
</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The current status of service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.AwaitableGetKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.AwaitableGetManagedKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetManagedKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetManagedKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.AwaitableGetServerlessKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetServerlessKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetServerlessKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">disk_category=None</em>, <em class="sig-param">disk_size=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">is_outdated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">need_slb=None</em>, <em class="sig-param">node_number=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">release_eip=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Cluster resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="method">
<dt id="pulumi_alicloud.cs.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">disk_category=None</em>, <em class="sig-param">disk_size=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">is_outdated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">need_slb=None</em>, <em class="sig-param">node_number=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">release_eip=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">slb_id=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesClusters.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetManagedKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedKubernetesClusters.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetServerlessKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">enable_details=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerlessKubernetesClusters.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cs.Kubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Kubernetes</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">cpu_policy=None</em>, <em class="sig-param">enable_ssh=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">install_cloud_monitor=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">master_auto_renew=None</em>, <em class="sig-param">master_auto_renew_period=None</em>, <em class="sig-param">master_disk_category=None</em>, <em class="sig-param">master_disk_size=None</em>, <em class="sig-param">master_instance_charge_type=None</em>, <em class="sig-param">master_instance_types=None</em>, <em class="sig-param">master_period=None</em>, <em class="sig-param">master_period_unit=None</em>, <em class="sig-param">master_vswitch_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">node_cidr_mask=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pod_cidr=None</em>, <em class="sig-param">pod_vswitch_ids=None</em>, <em class="sig-param">proxy_mode=None</em>, <em class="sig-param">service_cidr=None</em>, <em class="sig-param">slb_internet_enabled=None</em>, <em class="sig-param">user_ca=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">worker_auto_renew=None</em>, <em class="sig-param">worker_auto_renew_period=None</em>, <em class="sig-param">worker_data_disk_category=None</em>, <em class="sig-param">worker_data_disk_size=None</em>, <em class="sig-param">worker_disk_category=None</em>, <em class="sig-param">worker_disk_size=None</em>, <em class="sig-param">worker_instance_charge_type=None</em>, <em class="sig-param">worker_instance_types=None</em>, <em class="sig-param">worker_number=None</em>, <em class="sig-param">worker_period=None</em>, <em class="sig-param">worker_period_unit=None</em>, <em class="sig-param">worker_vswitch_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Kubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[str] cpu_policy: kubelet cpu policy. options: static|none. default: none.
:param pulumi.Input[bool] enable_ssh: Enable login to the node through SSH. default: false 
:param pulumi.Input[str] image_id: Custom Image support. Must based on CentOS7 or AliyunLinux2.
:param pulumi.Input[bool] install_cloud_monitor: Install cloud monitor agent on ECS. default: true 
:param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.
:param pulumi.Input[str] kube_config: The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.
:param pulumi.Input[bool] master_auto_renew: Enable master payment auto-renew, defaults to false.
:param pulumi.Input[float] master_auto_renew_period: Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[str] master_disk_category: The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.
:param pulumi.Input[float] master_disk_size: The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.
:param pulumi.Input[str] master_instance_charge_type: Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.
:param pulumi.Input[list] master_instance_types: The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.
:param pulumi.Input[float] master_period: Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.
:param pulumi.Input[str] master_period_unit: Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.
:param pulumi.Input[str] name: The kubernetes cluster’s name. It is unique in one Alicloud account.
:param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.
:param pulumi.Input[float] node_cidr_mask: The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24
:param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] pod_cidr: [Flannel Specific] The CIDR block for the pod network when using Flannel. 
:param pulumi.Input[list] pod_vswitch_ids: [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.
:param pulumi.Input[str] proxy_mode: Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.
:param pulumi.Input[str] service_cidr: The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
:param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
:param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
:param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
:param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
:param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[str] worker_disk_category: The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.
:param pulumi.Input[float] worker_disk_size: The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.
:param pulumi.Input[str] worker_instance_charge_type: Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.
:param pulumi.Input[list] worker_instance_types: The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.
:param pulumi.Input[float] worker_number: The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.
:param pulumi.Input[float] worker_period: Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.
:param pulumi.Input[str] worker_period_unit: Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.connections">
<code class="sig-name descname">connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Master node SSH IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service Access Domain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.cpu_policy">
<code class="sig-name descname">cpu_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.cpu_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>kubelet cpu policy. options: static|none. default: none.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.enable_ssh">
<code class="sig-name descname">enable_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.enable_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable login to the node through SSH. default: false</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom Image support. Must based on CentOS7 or AliyunLinux2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.install_cloud_monitor">
<code class="sig-name descname">install_cloud_monitor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.install_cloud_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Install cloud monitor agent on ECS. default: true</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.key_name">
<code class="sig-name descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_auto_renew">
<code class="sig-name descname">master_auto_renew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable master payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_auto_renew_period">
<code class="sig-name descname">master_auto_renew_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_disk_category">
<code class="sig-name descname">master_disk_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_disk_size">
<code class="sig-name descname">master_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_instance_charge_type">
<code class="sig-name descname">master_instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_instance_types">
<code class="sig-name descname">master_instance_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_nodes">
<code class="sig-name descname">master_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster master nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_period">
<code class="sig-name descname">master_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_period_unit">
<code class="sig-name descname">master_period_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is unique in one Alicloud account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.nat_gateway_id">
<code class="sig-name descname">nat_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of nat gateway used to launch kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.node_cidr_mask">
<code class="sig-name descname">node_cidr_mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.node_cidr_mask" title="Permalink to this definition">¶</a></dt>
<dd><p>The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.pod_cidr">
<code class="sig-name descname">pod_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.pod_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>[Flannel Specific] The CIDR block for the pod network when using Flannel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.pod_vswitch_ids">
<code class="sig-name descname">pod_vswitch_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.pod_vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>[Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.proxy_mode">
<code class="sig-name descname">proxy_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.proxy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of security group where the current cluster worker node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.service_cidr">
<code class="sig-name descname">service_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.service_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.slb_internet_enabled">
<code class="sig-name descname">slb_internet_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.slb_internet_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet load balancer for API Server. Default to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.slb_intranet">
<code class="sig-name descname">slb_intranet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.slb_intranet" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of private load balancer where the current cluster master node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.user_ca">
<code class="sig-name descname">user_ca</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.user_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_auto_renew">
<code class="sig-name descname">worker_auto_renew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable worker payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_auto_renew_period">
<code class="sig-name descname">worker_auto_renew_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_disk_category">
<code class="sig-name descname">worker_disk_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_disk_size">
<code class="sig-name descname">worker_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_instance_charge_type">
<code class="sig-name descname">worker_instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_instance_types">
<code class="sig-name descname">worker_instance_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_nodes">
<code class="sig-name descname">worker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_number">
<code class="sig-name descname">worker_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_period">
<code class="sig-name descname">worker_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_period_unit">
<code class="sig-name descname">worker_period_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Kubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">connections=None</em>, <em class="sig-param">cpu_policy=None</em>, <em class="sig-param">enable_ssh=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">install_cloud_monitor=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">master_auto_renew=None</em>, <em class="sig-param">master_auto_renew_period=None</em>, <em class="sig-param">master_disk_category=None</em>, <em class="sig-param">master_disk_size=None</em>, <em class="sig-param">master_instance_charge_type=None</em>, <em class="sig-param">master_instance_types=None</em>, <em class="sig-param">master_nodes=None</em>, <em class="sig-param">master_period=None</em>, <em class="sig-param">master_period_unit=None</em>, <em class="sig-param">master_vswitch_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">nat_gateway_id=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">node_cidr_mask=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pod_cidr=None</em>, <em class="sig-param">pod_vswitch_ids=None</em>, <em class="sig-param">proxy_mode=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">service_cidr=None</em>, <em class="sig-param">slb_id=None</em>, <em class="sig-param">slb_internet=None</em>, <em class="sig-param">slb_internet_enabled=None</em>, <em class="sig-param">slb_intranet=None</em>, <em class="sig-param">user_ca=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">worker_auto_renew=None</em>, <em class="sig-param">worker_auto_renew_period=None</em>, <em class="sig-param">worker_data_disk_category=None</em>, <em class="sig-param">worker_data_disk_size=None</em>, <em class="sig-param">worker_disk_category=None</em>, <em class="sig-param">worker_disk_size=None</em>, <em class="sig-param">worker_instance_charge_type=None</em>, <em class="sig-param">worker_instance_types=None</em>, <em class="sig-param">worker_nodes=None</em>, <em class="sig-param">worker_number=None</em>, <em class="sig-param">worker_period=None</em>, <em class="sig-param">worker_period_unit=None</em>, <em class="sig-param">worker_vswitch_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Kubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p></li>
<li><p><strong>cpu_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – kubelet cpu policy. options: static|none. default: none.</p></li>
<li><p><strong>enable_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable login to the node through SSH. default: false</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom Image support. Must based on CentOS7 or AliyunLinux2.</p></li>
<li><p><strong>install_cloud_monitor</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Install cloud monitor agent on ECS. default: true</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>master_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable master payment auto-renew, defaults to false.</p></li>
<li><p><strong>master_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>master_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>master_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.</p></li>
<li><p><strong>master_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>master_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>master_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster master nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>master_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>master_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of nat gateway used to launch kubernetes cluster.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p></li>
<li><p><strong>node_cidr_mask</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>pod_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – [Flannel Specific] The CIDR block for the pod network when using Flannel.</p></li>
<li><p><strong>pod_vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.</p></li>
<li><p><strong>proxy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of security group where the current cluster worker node is located.</p></li>
<li><p><strong>service_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p></li>
<li><p><strong>slb_internet_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet load balancer for API Server. Default to true.</p></li>
<li><p><strong>slb_intranet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of private load balancer where the current cluster master node is located.</p></li>
<li><p><strong>user_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>worker_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable worker payment auto-renew, defaults to false.</p></li>
<li><p><strong>worker_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>connections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Master node SSH IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service Access Domain.</p></li>
</ul>
<p>The <strong>master_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
<p>The <strong>worker_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Kubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Kubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">KubernetesAutoscaler</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cool_down_duration=None</em>, <em class="sig-param">defer_scale_in_duration=None</em>, <em class="sig-param">nodepools=None</em>, <em class="sig-param">utilization=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager cluster-autoscaler in Kubernetes Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The scaling group must use CentOS7 or AliyunLinux2 as base image.</p>
<p><strong>NOTE:</strong> The cluster-autoscaler can only use the same size of instanceTypes in one scaling group.</p>
<p><strong>NOTE:</strong> Add Policy to RAM role of the node to deploy cluster-autoscaler if you need.</p>
<p><strong>NOTE:</strong> Available in 1.65.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of kubernetes cluster.</p></li>
<li><p><strong>cool_down_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cool_down_duration option of cluster-autoscaler.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>defer_scale_in_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The defer_scale_in_duration option of cluster-autoscaler.</p></li>
<li><p><strong>nodepools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>utilization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The utilization option of cluster-autoscaler.</p>
</dd>
</dl>
<p>The <strong>nodepools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.cool_down_duration">
<code class="sig-name descname">cool_down_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.cool_down_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The cool_down_duration option of cluster-autoscaler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.defer_scale_in_duration">
<code class="sig-name descname">defer_scale_in_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.defer_scale_in_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The defer_scale_in_duration option of cluster-autoscaler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.nodepools">
<code class="sig-name descname">nodepools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.nodepools" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.id</span></code> - (Required) The scaling group id of the groups configured for cluster-autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.taints</span></code> - (Required) The taints for the nodes in scaling group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.labels</span></code> - (Required) The labels for the nodes in scaling group.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.utilization">
<code class="sig-name descname">utilization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.utilization" title="Permalink to this definition">¶</a></dt>
<dd><p>The utilization option of cluster-autoscaler.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cool_down_duration=None</em>, <em class="sig-param">defer_scale_in_duration=None</em>, <em class="sig-param">nodepools=None</em>, <em class="sig-param">utilization=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesAutoscaler resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of kubernetes cluster.</p></li>
<li><p><strong>cool_down_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cool_down_duration option of cluster-autoscaler.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>defer_scale_in_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The defer_scale_in_duration option of cluster-autoscaler.</p></li>
<li><p><strong>nodepools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>utilization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The utilization option of cluster-autoscaler.</p>
</dd>
</dl>
<p>The <strong>nodepools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ManagedKubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">ManagedKubernetes</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">cpu_policy=None</em>, <em class="sig-param">enable_ssh=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">install_cloud_monitor=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">node_cidr_mask=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pod_cidr=None</em>, <em class="sig-param">pod_vswitch_ids=None</em>, <em class="sig-param">proxy_mode=None</em>, <em class="sig-param">service_cidr=None</em>, <em class="sig-param">slb_internet_enabled=None</em>, <em class="sig-param">user_ca=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">worker_auto_renew=None</em>, <em class="sig-param">worker_auto_renew_period=None</em>, <em class="sig-param">worker_data_disk_category=None</em>, <em class="sig-param">worker_data_disk_size=None</em>, <em class="sig-param">worker_disk_category=None</em>, <em class="sig-param">worker_disk_size=None</em>, <em class="sig-param">worker_instance_charge_type=None</em>, <em class="sig-param">worker_instance_types=None</em>, <em class="sig-param">worker_number=None</em>, <em class="sig-param">worker_period=None</em>, <em class="sig-param">worker_period_unit=None</em>, <em class="sig-param">worker_vswitch_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ManagedKubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[str] cpu_policy: kubelet cpu policy. options: static|none. default: none.
:param pulumi.Input[bool] enable_ssh: Enable login to the node through SSH. default: false 
:param pulumi.Input[str] image_id: Custom Image support. Must based on CentOS7 or AliyunLinux2.
:param pulumi.Input[bool] install_cloud_monitor: Install cloud monitor agent on ECS. default: true 
:param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.
:param pulumi.Input[str] kube_config: The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.
:param pulumi.Input[str] name: The kubernetes cluster’s name. It is unique in one Alicloud account.
:param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.
:param pulumi.Input[float] node_cidr_mask: The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24
:param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] pod_cidr: [Flannel Specific] The CIDR block for the pod network when using Flannel. 
:param pulumi.Input[list] pod_vswitch_ids: [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.
:param pulumi.Input[str] proxy_mode: Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.
:param pulumi.Input[str] service_cidr: The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
:param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
:param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
:param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
:param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
:param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[str] worker_disk_category: The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.
:param pulumi.Input[float] worker_disk_size: The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.
:param pulumi.Input[str] worker_instance_charge_type: Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.
:param pulumi.Input[list] worker_instance_types: The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.
:param pulumi.Input[float] worker_number: The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.
:param pulumi.Input[float] worker_period: Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.
:param pulumi.Input[str] worker_period_unit: Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.connections">
<code class="sig-name descname">connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service Access Domain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.cpu_policy">
<code class="sig-name descname">cpu_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.cpu_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>kubelet cpu policy. options: static|none. default: none.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.enable_ssh">
<code class="sig-name descname">enable_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.enable_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable login to the node through SSH. default: false</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom Image support. Must based on CentOS7 or AliyunLinux2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.install_cloud_monitor">
<code class="sig-name descname">install_cloud_monitor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.install_cloud_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Install cloud monitor agent on ECS. default: true</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.key_name">
<code class="sig-name descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is unique in one Alicloud account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.nat_gateway_id">
<code class="sig-name descname">nat_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of nat gateway used to launch kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.node_cidr_mask">
<code class="sig-name descname">node_cidr_mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.node_cidr_mask" title="Permalink to this definition">¶</a></dt>
<dd><p>The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.pod_cidr">
<code class="sig-name descname">pod_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.pod_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>[Flannel Specific] The CIDR block for the pod network when using Flannel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.pod_vswitch_ids">
<code class="sig-name descname">pod_vswitch_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.pod_vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>[Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.proxy_mode">
<code class="sig-name descname">proxy_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.proxy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of security group where the current cluster worker node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.service_cidr">
<code class="sig-name descname">service_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.service_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.slb_internet_enabled">
<code class="sig-name descname">slb_internet_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.slb_internet_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet load balancer for API Server. Default to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.slb_intranet">
<code class="sig-name descname">slb_intranet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.slb_intranet" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of private load balancer where the current cluster master node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.user_ca">
<code class="sig-name descname">user_ca</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.user_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew">
<code class="sig-name descname">worker_auto_renew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable worker payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew_period">
<code class="sig-name descname">worker_auto_renew_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_disk_category">
<code class="sig-name descname">worker_disk_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_disk_size">
<code class="sig-name descname">worker_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_instance_charge_type">
<code class="sig-name descname">worker_instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_instance_types">
<code class="sig-name descname">worker_instance_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_nodes">
<code class="sig-name descname">worker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_number">
<code class="sig-name descname">worker_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_period">
<code class="sig-name descname">worker_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_period_unit">
<code class="sig-name descname">worker_period_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">connections=None</em>, <em class="sig-param">cpu_policy=None</em>, <em class="sig-param">enable_ssh=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">install_cloud_monitor=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">nat_gateway_id=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">node_cidr_mask=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pod_cidr=None</em>, <em class="sig-param">pod_vswitch_ids=None</em>, <em class="sig-param">proxy_mode=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">service_cidr=None</em>, <em class="sig-param">slb_id=None</em>, <em class="sig-param">slb_internet=None</em>, <em class="sig-param">slb_internet_enabled=None</em>, <em class="sig-param">slb_intranet=None</em>, <em class="sig-param">user_ca=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">worker_auto_renew=None</em>, <em class="sig-param">worker_auto_renew_period=None</em>, <em class="sig-param">worker_data_disk_category=None</em>, <em class="sig-param">worker_data_disk_size=None</em>, <em class="sig-param">worker_disk_category=None</em>, <em class="sig-param">worker_disk_size=None</em>, <em class="sig-param">worker_instance_charge_type=None</em>, <em class="sig-param">worker_instance_types=None</em>, <em class="sig-param">worker_nodes=None</em>, <em class="sig-param">worker_number=None</em>, <em class="sig-param">worker_period=None</em>, <em class="sig-param">worker_period_unit=None</em>, <em class="sig-param">worker_vswitch_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedKubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p></li>
<li><p><strong>cpu_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – kubelet cpu policy. options: static|none. default: none.</p></li>
<li><p><strong>enable_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable login to the node through SSH. default: false</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom Image support. Must based on CentOS7 or AliyunLinux2.</p></li>
<li><p><strong>install_cloud_monitor</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Install cloud monitor agent on ECS. default: true</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of nat gateway used to launch kubernetes cluster.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p></li>
<li><p><strong>node_cidr_mask</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>pod_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – [Flannel Specific] The CIDR block for the pod network when using Flannel.</p></li>
<li><p><strong>pod_vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.</p></li>
<li><p><strong>proxy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of security group where the current cluster worker node is located.</p></li>
<li><p><strong>service_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p></li>
<li><p><strong>slb_internet_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet load balancer for API Server. Default to true.</p></li>
<li><p><strong>slb_intranet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of private load balancer where the current cluster master node is located.</p></li>
<li><p><strong>user_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>worker_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable worker payment auto-renew, defaults to false.</p></li>
<li><p><strong>worker_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>connections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service Access Domain.</p></li>
</ul>
<p>The <strong>worker_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ManagedKubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ServerlessKubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">ServerlessKubernetes</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">endpoint_public_access_enabled=None</em>, <em class="sig-param">force_update=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">private_zone=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServerlessKubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[bool] deletion_protection: Whether enable the deletion protection or not.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_public_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet  eip for API Server. Default to false.</p></li>
<li><p><strong>force_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p></li>
<li><p><strong>private_zone</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default nil, A map of tags assigned to the kubernetes cluster .</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enable the deletion protection or not.</p>
<ul class="simple">
<li><p>true: Enable deletion protection.</p></li>
<li><p>false: Disable deletion protection.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.endpoint_public_access_enabled">
<code class="sig-name descname">endpoint_public_access_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.endpoint_public_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet  eip for API Server. Default to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.force_update">
<code class="sig-name descname">force_update</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.force_update" title="Permalink to this definition">¶</a></dt>
<dd><p>Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.private_zone">
<code class="sig-name descname">private_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.private_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Default nil, A map of tags assigned to the kubernetes cluster .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">cluster_ca_cert=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">endpoint_public_access_enabled=None</em>, <em class="sig-param">force_update=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">new_nat_gateway=None</em>, <em class="sig-param">private_zone=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerlessKubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether enable the deletion protection or not.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_public_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet  eip for API Server. Default to false.</p></li>
<li><p><strong>force_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p></li>
<li><p><strong>private_zone</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default nil, A map of tags assigned to the kubernetes cluster .</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Swarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Swarm</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">disk_category=None</em>, <em class="sig-param">disk_size=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">is_outdated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">need_slb=None</em>, <em class="sig-param">node_number=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">release_eip=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>DEPRECATED:</strong> This resource manages swarm cluster, which is being deprecated and will be replaced by Kubernetes cluster.</p>
</div></blockquote>
<p>This resource will help you to manager a Swarm Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Swarm cluster only supports VPC network and you can specify a VPC network by filed <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">172.19</span><span class="o">-</span><span class="mf">30.0</span><span class="o">.</span><span class="mi">0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID of ECS instance node used. Default to System automate allocated.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ECS instance node.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>node_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node.</p></li>
<li><p><strong>release_eip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to release EIP after creating swarm cluster successfully. Default to false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `need_slb`- (ForceNew) Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.agent_version">
<code class="sig-name descname">agent_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The nodes agent version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p>
<ul class="simple">
<li><p>192.168.0.0/16</p></li>
<li><p>172.19-30.0.0/16</p></li>
<li><p>10.0.0.0/16</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.disk_category">
<code class="sig-name descname">disk_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.disk_size">
<code class="sig-name descname">disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID of ECS instance node used. Default to System automate allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of ECS instance node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.is_outdated">
<code class="sig-name descname">is_outdated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.is_outdated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use outdated instance type. Default to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The container cluster’s name. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.node_number">
<code class="sig-name descname">node_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.node_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.nodes">
<code class="sig-name descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Elastic IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The node current status. It is different with instance status.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ECS instance node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.release_eip">
<code class="sig-name descname">release_eip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.release_eip" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to release EIP after creating swarm cluster successfully. Default to false.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">need_slb</span></code>- (ForceNew) Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of security group where the current cluster worker node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.slb_id">
<code class="sig-name descname">slb_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.slb_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of load balancer where the current cluster worker node is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cs.Swarm.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Swarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_version=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">disk_category=None</em>, <em class="sig-param">disk_size=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">is_outdated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">need_slb=None</em>, <em class="sig-param">node_number=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">release_eip=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">slb_id=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Swarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The nodes agent version.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">172.19</span><span class="o">-</span><span class="mf">30.0</span><span class="o">.</span><span class="mi">0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID of ECS instance node used. Default to System automate allocated.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ECS instance node.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>node_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node.</p></li>
<li><p><strong>release_eip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to release EIP after creating swarm cluster successfully. Default to false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `need_slb`- (ForceNew) Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of security group where the current cluster worker node is located.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p></li>
<li><p><strong>slb_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of load balancer where the current cluster worker node is located.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elastic IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The node current status. It is different with instance status.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cs.Swarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Swarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.get_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param">enable_details=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.34.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cs.get_managed_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_managed_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param">enable_details=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_managed_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Managed Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.35.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cs.get_serverless_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_serverless_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param">enable_details=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_serverless_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Serverless Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.58.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
