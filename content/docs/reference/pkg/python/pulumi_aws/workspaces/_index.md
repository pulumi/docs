---
title: Module workspaces
title_tag: Module workspaces | Package pulumi_aws | Python SDK
linktitle: workspaces
notitle: true
---

<div class="section" id="workspaces">
<h1>workspaces<a class="headerlink" href="#workspaces" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.workspaces"></span><dl class="py class">
<dt id="pulumi_aws.workspaces.AwaitableGetBundleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">AwaitableGetBundleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bundle_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_storages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_storages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.AwaitableGetBundleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.workspaces.Directory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">Directory</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_service_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.Directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a directory registration in AWS WorkSpaces Service</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">main_vpc</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Vpc</span><span class="p">(</span><span class="s2">&quot;mainVpc&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/16&quot;</span><span class="p">)</span>
<span class="n">private_a</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;private-a&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="s2">&quot;us-east-1a&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">private_b</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;private-b&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="s2">&quot;us-east-1b&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">main_directory</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">directoryservice</span><span class="o">.</span><span class="n">Directory</span><span class="p">(</span><span class="s2">&quot;mainDirectory&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;#S1ncerely&quot;</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="s2">&quot;Small&quot;</span><span class="p">,</span>
    <span class="n">vpc_settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;subnetIds&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="n">private_a</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">private_b</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;vpcId&quot;</span><span class="p">:</span> <span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">main_workspaces_directory_directory</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">workspaces</span><span class="o">.</span><span class="n">Directory</span><span class="p">(</span><span class="s2">&quot;mainWorkspaces/directoryDirectory&quot;</span><span class="p">,</span>
    <span class="n">directory_id</span><span class="o">=</span><span class="n">main_directory</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">self_service_permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;increaseVolumeSize&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;rebuildWorkspace&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory identifier for registration in WorkSpaces service.</p></li>
<li><p><strong>self_service_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The permissions to enable or disable self-service capabilities.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identifiers of the subnets where the directory resides.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags assigned to the WorkSpaces directory.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>self_service_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changeComputeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">increaseVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rebuildWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can restart their workspace. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">switchRunningMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can switch the running mode of their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.alias">
<code class="sig-name descname">alias</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory alias.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.customer_user_name">
<code class="sig-name descname">customer_user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.customer_user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user name for the service account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.directory_id">
<code class="sig-name descname">directory_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory identifier for registration in WorkSpaces service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.directory_name">
<code class="sig-name descname">directory_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.directory_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.directory_type">
<code class="sig-name descname">directory_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.directory_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.dns_ip_addresses">
<code class="sig-name descname">dns_ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.dns_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses of the DNS servers for the directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.iam_role_id">
<code class="sig-name descname">iam_role_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.iam_role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.ip_group_ids">
<code class="sig-name descname">ip_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.ip_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers of the IP access control groups associated with the directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.registration_code">
<code class="sig-name descname">registration_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.registration_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.self_service_permissions">
<code class="sig-name descname">self_service_permissions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.self_service_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions to enable or disable self-service capabilities.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changeComputeType</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">increaseVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rebuildWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether WorkSpaces directory users can restart their workspace. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">switchRunningMode</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether WorkSpaces directory users can switch the running mode of their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers of the subnets where the directory resides.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the WorkSpaces directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.Directory.workspace_security_group_id">
<code class="sig-name descname">workspace_security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.Directory.workspace_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the security group that is assigned to new WorkSpaces.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.workspaces.Directory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directory_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directory_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_role_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_service_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workspace_security_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.Directory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Directory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory alias.</p></li>
<li><p><strong>customer_user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user name for the service account.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory identifier for registration in WorkSpaces service.</p></li>
<li><p><strong>directory_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the directory.</p></li>
<li><p><strong>directory_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory type.</p></li>
<li><p><strong>dns_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses of the DNS servers for the directory.</p></li>
<li><p><strong>iam_role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.</p></li>
<li><p><strong>ip_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identifiers of the IP access control groups associated with the directory.</p></li>
<li><p><strong>registration_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.</p></li>
<li><p><strong>self_service_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The permissions to enable or disable self-service capabilities.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identifiers of the subnets where the directory resides.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags assigned to the WorkSpaces directory.</p></li>
<li><p><strong>workspace_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the security group that is assigned to new WorkSpaces.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>self_service_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changeComputeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">increaseVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rebuildWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartWorkspace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can restart their workspace. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">switchRunningMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether WorkSpaces directory users can switch the running mode of their workspace. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.workspaces.Directory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.Directory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.workspaces.Directory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.Directory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.workspaces.GetBundleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">GetBundleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bundle_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_storages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_storages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBundle.</p>
<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.compute_types">
<code class="sig-name descname">compute_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.compute_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute type. See supported fields below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the bundle.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the compute type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the bundle.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.root_storages">
<code class="sig-name descname">root_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.root_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The root volume. See supported fields below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.user_storages">
<code class="sig-name descname">user_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.user_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The user storage. See supported fields below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.workspaces.IpGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">IpGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IP access control group in AWS WorkSpaces Service</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">contractors</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">workspaces</span><span class="o">.</span><span class="n">IpGroup</span><span class="p">(</span><span class="s2">&quot;contractors&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Contractors IP access control group&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IP group.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range, in CIDR notation, e.g. <code class="docutils literal notranslate"><span class="pre">10.0.0.0/16</span></code></p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.workspaces.IpGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.IpGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IP group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.workspaces.IpGroup.rules">
<code class="sig-name descname">rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address range, in CIDR notation, e.g. <code class="docutils literal notranslate"><span class="pre">10.0.0.0/16</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.workspaces.IpGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IP group.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range, in CIDR notation, e.g. <code class="docutils literal notranslate"><span class="pre">10.0.0.0/16</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.workspaces.IpGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.workspaces.IpGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.IpGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.workspaces.get_bundle">
<code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">get_bundle</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bundle_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.get_bundle" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a WorkSpaces Bundle.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">workspaces</span><span class="o">.</span><span class="n">get_bundle</span><span class="p">(</span><span class="n">bundle_id</span><span class="o">=</span><span class="s2">&quot;wsb-b0s22j3d7&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>bundle_id</strong> (<em>str</em>) – The ID of the bundle.</p>
</dd>
</dl>
</dd></dl>

</div>
