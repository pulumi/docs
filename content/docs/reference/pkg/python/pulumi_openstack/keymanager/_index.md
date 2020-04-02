---
title: Module keymanager
title_tag: Module keymanager | Package pulumi_openstack | Python SDK
linktitle: keymanager
notitle: true
---

<div class="section" id="keymanager">
<h1>keymanager<a class="headerlink" href="#keymanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.keymanager"></span><dl class="class">
<dt id="pulumi_openstack.keymanager.AwaitableGetContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">AwaitableGetContainerResult</code><span class="sig-paren">(</span><em class="sig-param">acls=None</em>, <em class="sig-param">consumers=None</em>, <em class="sig-param">container_ref=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_refs=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.AwaitableGetContainerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.keymanager.AwaitableGetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">AwaitableGetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">acl_only=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">bit_length=None</em>, <em class="sig-param">content_types=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">created_at_filter=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">expiration_filter=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">payload=None</em>, <em class="sig-param">payload_content_encoding=None</em>, <em class="sig-param">payload_content_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_ref=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">updated_at_filter=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.AwaitableGetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.keymanager.ContainerV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">ContainerV1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_refs=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 Barbican container resource within OpenStack.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows to control an access to a container. Currently only
the <code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the container is
accessible project wide. The <code class="docutils literal notranslate"><span class="pre">read</span></code> structure is described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a container. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 container.</p></li>
<li><p><strong>secret_refs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries containing references to secrets. The structure is described
below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to indicate the type of container. Must be one of <code class="docutils literal notranslate"><span class="pre">generic</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the container ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the container is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the container ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of user IDs, which are allowed to access the
container, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>secret_refs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_ref</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret reference / where to find the secret, URL.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows to control an access to a container. Currently only
the <code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the container is
accessible project wide. The <code class="docutils literal notranslate"><span class="pre">read</span></code> structure is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The date the container ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the container is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The date the container ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of user IDs, which are allowed to access the
container, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.consumers">
<code class="sig-name descname">consumers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.consumers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of the container consumers. The structure is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The consumer URL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.container_ref">
<code class="sig-name descname">container_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.container_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The container reference / where to find the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the container ACL was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.creator_id">
<code class="sig-name descname">creator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.creator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The creator of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a container. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.secret_refs">
<code class="sig-name descname">secret_refs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.secret_refs" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of dictionaries containing references to secrets. The structure is described
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_ref</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret reference / where to find the secret, URL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to indicate the type of container. Must be one of <code class="docutils literal notranslate"><span class="pre">generic</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.ContainerV1.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the container ACL was last updated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.keymanager.ContainerV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">consumers=None</em>, <em class="sig-param">container_ref=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_refs=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ContainerV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows to control an access to a container. Currently only
the <code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the container is
accessible project wide. The <code class="docutils literal notranslate"><span class="pre">read</span></code> structure is described below.</p></li>
<li><p><strong>consumers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of the container consumers. The structure is described below.</p></li>
<li><p><strong>container_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container reference / where to find the container.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the container ACL was created.</p></li>
<li><p><strong>creator_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creator of the container.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p>
</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a container. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 container.</p></li>
<li><p><strong>secret_refs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries containing references to secrets. The structure is described
below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the container.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to indicate the type of container. Must be one of <code class="docutils literal notranslate"><span class="pre">generic</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the container ACL was last updated.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the container ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the container is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the container ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of user IDs, which are allowed to access the
container, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>consumers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The consumer URL.</p></li>
</ul>
<p>The <strong>secret_refs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the secret reference. The reference names must correspond the container type, more details are available <a class="reference external" href="https://docs.openstack.org/barbican/stein/api/reference/containers.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_ref</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret reference / where to find the secret, URL.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.keymanager.ContainerV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.keymanager.ContainerV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.ContainerV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.keymanager.GetContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">GetContainerResult</code><span class="sig-paren">(</span><em class="sig-param">acls=None</em>, <em class="sig-param">consumers=None</em>, <em class="sig-param">container_ref=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_refs=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getContainer.</p>
<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of ACLs assigned to a container. The <code class="docutils literal notranslate"><span class="pre">read</span></code> structure is
described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.consumers">
<code class="sig-name descname">consumers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.consumers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of the container consumers. The structure is described
below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.container_ref">
<code class="sig-name descname">container_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.container_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The container reference / where to find the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the container ACL was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.creator_id">
<code class="sig-name descname">creator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.creator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The creator of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the consumer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.secret_refs">
<code class="sig-name descname">secret_refs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.secret_refs" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of dictionaries containing references to secrets. The
structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The container type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetContainerResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetContainerResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the container ACL was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.keymanager.GetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">GetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">acl_only=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">bit_length=None</em>, <em class="sig-param">content_types=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">created_at_filter=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">expiration_filter=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">payload=None</em>, <em class="sig-param">payload_content_encoding=None</em>, <em class="sig-param">payload_content_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_ref=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">updated_at_filter=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.acl_only">
<code class="sig-name descname">acl_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.acl_only" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of ACLs assigned to a secret. The <code class="docutils literal notranslate"><span class="pre">read</span></code> structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.bit_length">
<code class="sig-name descname">bit_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.bit_length" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.content_types">
<code class="sig-name descname">content_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.content_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of the content types, assigned on the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the secret ACL was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.created_at_filter">
<code class="sig-name descname">created_at_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.created_at_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.creator_id">
<code class="sig-name descname">creator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.creator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The creator of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.expiration">
<code class="sig-name descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the secret will expire.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.expiration_filter">
<code class="sig-name descname">expiration_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.expiration_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.payload">
<code class="sig-name descname">payload</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.payload" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret payload.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.payload_content_encoding">
<code class="sig-name descname">payload_content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.payload_content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secret encoding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.payload_content_type">
<code class="sig-name descname">payload_content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.payload_content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secret content type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.secret_ref">
<code class="sig-name descname">secret_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.secret_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret reference / where to find the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.secret_type">
<code class="sig-name descname">secret_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.secret_type" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the secret ACL was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.GetSecretResult.updated_at_filter">
<code class="sig-name descname">updated_at_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.GetSecretResult.updated_at_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.keymanager.SecretV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">SecretV1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">bit_length=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">payload=None</em>, <em class="sig-param">payload_content_encoding=None</em>, <em class="sig-param">payload_content_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretV1 resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] acl: Allows to control an access to a secret. Currently only the</p>
<blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the secret is accessible
project wide.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>bit_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the secret in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted, a secret will never expire. Changing this creates a new secret.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional Metadata for the secret.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Secret. Does not have
to be unique.</p></li>
<li><p><strong>payload</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret’s data to be stored. <strong>payload_content_type</strong> must also be supplied if <strong>payload</strong> is included.</p></li>
<li><p><strong>payload_content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (required if <strong>payload</strong> is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either <code class="docutils literal notranslate"><span class="pre">base64</span></code> or <code class="docutils literal notranslate"><span class="pre">binary</span></code>.</p></li>
<li><p><strong>payload_content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (required if <strong>payload</strong> is included) The media type for the content of the payload. Must be one of <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;</span> <span class="pre">charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>, <code class="docutils literal notranslate"><span class="pre">application/pkcs8</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a secret. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 secret.</p></li>
<li><p><strong>secret_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to indicate the type of secret being stored. For more information see <a class="reference external" href="https://docs.openstack.org/barbican/latest/api/reference/secret_types.html">Secret types</a>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the secret ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the secret is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the secret ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of user IDs, which are allowed to access the
secret, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.acl">
<code class="sig-name descname">acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows to control an access to a secret. Currently only the
<code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the secret is accessible
project wide.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The date the secret ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the secret is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The date the secret ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of user IDs, which are allowed to access the
secret, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata provided by a user or system for informational purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.all_metadata">
<code class="sig-name descname">all_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.all_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.bit_length">
<code class="sig-name descname">bit_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.bit_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata provided by a user or system for informational purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.content_types">
<code class="sig-name descname">content_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.content_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of the content types, assigned on the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the secret ACL was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.creator_id">
<code class="sig-name descname">creator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.creator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The creator of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.expiration">
<code class="sig-name descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration time of the secret in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted, a secret will never expire. Changing this creates a new secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional Metadata for the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata provided by a user or system for informational purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the Secret. Does not have
to be unique.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.payload">
<code class="sig-name descname">payload</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.payload" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret’s data to be stored. <strong>payload_content_type</strong> must also be supplied if <strong>payload</strong> is included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.payload_content_encoding">
<code class="sig-name descname">payload_content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.payload_content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>(required if <strong>payload</strong> is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either <code class="docutils literal notranslate"><span class="pre">base64</span></code> or <code class="docutils literal notranslate"><span class="pre">binary</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.payload_content_type">
<code class="sig-name descname">payload_content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.payload_content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>(required if <strong>payload</strong> is included) The media type for the content of the payload. Must be one of <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;</span> <span class="pre">charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>, <code class="docutils literal notranslate"><span class="pre">application/pkcs8</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a secret. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.secret_ref">
<code class="sig-name descname">secret_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.secret_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret reference / where to find the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.secret_type">
<code class="sig-name descname">secret_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.secret_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to indicate the type of secret being stored. For more information see <a class="reference external" href="https://docs.openstack.org/barbican/latest/api/reference/secret_types.html">Secret types</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.keymanager.SecretV1.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the secret ACL was last updated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.keymanager.SecretV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">all_metadata=None</em>, <em class="sig-param">bit_length=None</em>, <em class="sig-param">content_types=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">creator_id=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">payload=None</em>, <em class="sig-param">payload_content_encoding=None</em>, <em class="sig-param">payload_content_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_ref=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows to control an access to a secret. Currently only the
<code class="docutils literal notranslate"><span class="pre">read</span></code> operation is supported. If not specified, the secret is accessible
project wide.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>all_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.</p></li>
<li><p><strong>bit_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>content_types</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of the content types, assigned on the secret.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the secret ACL was created.</p></li>
<li><p><strong>creator_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creator of the secret.</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the secret in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted, a secret will never expire. Changing this creates a new secret.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional Metadata for the secret.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Metadata provided by a user or system for informational purposes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Secret. Does not have
to be unique.</p></li>
<li><p><strong>payload</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret’s data to be stored. <strong>payload_content_type</strong> must also be supplied if <strong>payload</strong> is included.</p></li>
<li><p><strong>payload_content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (required if <strong>payload</strong> is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either <code class="docutils literal notranslate"><span class="pre">base64</span></code> or <code class="docutils literal notranslate"><span class="pre">binary</span></code>.</p></li>
<li><p><strong>payload_content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (required if <strong>payload</strong> is included) The media type for the content of the payload. Must be one of <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">text/plain;</span> <span class="pre">charset=utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>, <code class="docutils literal notranslate"><span class="pre">application/pkcs8</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to create a secret. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
V1 secret.</p></li>
<li><p><strong>secret_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret reference / where to find the secret.</p></li>
<li><p><strong>secret_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Used to indicate the type of secret being stored. For more information see <a class="reference external" href="https://docs.openstack.org/barbican/latest/api/reference/secret_types.html">Secret types</a>.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the secret.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the secret ACL was last updated.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acl</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the secret ACL was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the secret is accessible project wide.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date the secret ACL was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of user IDs, which are allowed to access the
secret, when <code class="docutils literal notranslate"><span class="pre">project_access</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.keymanager.SecretV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.keymanager.SecretV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.SecretV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.keymanager.get_container">
<code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">get_container</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.get_container" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available Barbican container.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/keymanager_container_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/keymanager_container_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The Container name.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a container. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code>
argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.keymanager.get_secret">
<code class="sig-prename descclassname">pulumi_openstack.keymanager.</code><code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param">acl_only=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">bit_length=None</em>, <em class="sig-param">created_at_filter=None</em>, <em class="sig-param">expiration_filter=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">updated_at_filter=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.keymanager.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>acl_only</strong> (<em>bool</em>) – Select the Secret with an ACL that contains the user.
Project scope is ignored. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>algorithm</strong> (<em>str</em>) – The Secret algorithm.</p></li>
<li><p><strong>bit_length</strong> (<em>float</em>) – The Secret bit length.</p></li>
<li><p><strong>created_at_filter</strong> (<em>str</em>) – Date filter to select the Secret with
created matching the specified criteria. See Date Filters below for more
detail.</p></li>
<li><p><strong>expiration_filter</strong> (<em>str</em>) – Date filter to select the Secret with
expiration matching the specified criteria. See Date Filters below for more
detail.</p></li>
<li><p><strong>mode</strong> (<em>str</em>) – The Secret mode.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The Secret name.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a secret. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code>
argument of the provider is used.</p></li>
<li><p><strong>secret_type</strong> (<em>str</em>) – <p>The Secret type. For more information see
<a class="reference external" href="https://docs.openstack.org/barbican/latest/api/reference/secret_types.html">Secret types</a>.</p>
</p></li>
<li><p><strong>updated_at_filter</strong> (<em>str</em>) – Date filter to select the Secret with
updated matching the specified criteria. See Date Filters below for more
detail.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
